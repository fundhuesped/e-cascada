#!/usr/bin/python
# -*- coding: utf-8 -*-

import calendar
import datetime as dt

import reversion

from datetime import datetime
from django.db import transaction
from django.db.models import Max
from django.db.models import Q
from django.utils.translation import gettext as _
from hc_core.exceptions import FailedDependencyException
from hc_practicas.models import Agenda
from hc_practicas.models import Ausencia
from hc_practicas.models import DayOfWeek
from hc_practicas.models import Period
from hc_practicas.models import Turno
from hc_practicas.models import TurnoSlot
from hc_practicas.serializers import PeriodNestSerializer
from hc_practicas.serializers import PrestacionNestedSerializer
from hc_practicas.serializers import ProfesionalNestedSerializer
from hc_practicas.services import turnoSlot_service

from rest_framework import serializers


class AgendaListSerializer(serializers.HyperlinkedModelSerializer):
    """
    AgendaListSerializer for list method only
    """
    id = serializers.ReadOnlyField()

    profesional = ProfesionalNestedSerializer(
        many=False
    )

    prestacion = PrestacionNestedSerializer(
        many=False
    )
    class Meta:
        """
        AgendaListSerializer meta configuration
        """
        model = Agenda
        fields = ('id', 'status', 'start', 'end', 'validFrom', 'validTo', 'profesional', 'prestacion')

class AgendaNestSerializer(serializers.HyperlinkedModelSerializer):
    """
    AgendaNestSerializer for all methods except list
    """
    id = serializers.ReadOnlyField()

    periods = PeriodNestSerializer(
        many=True
    )

    profesional = ProfesionalNestedSerializer(
        many=False
    )

    prestacion = PrestacionNestedSerializer(
        many=False
    )

    def get_from_date(self, profesional, prestacion):
        """
        Obtiene la fecha desde la cual se debe crear una agenda para 
        un profesional y una prestación dada
        :param profesional:
        :param prestacion:
        :return:
        """

        #Filtrado de agenda por profesional y prestación
        queryset = Agenda.objects.filter(profesional=profesional, prestacion=prestacion)

        if queryset.count() > 0:
            max_date = queryset.aggregate(Max('validTo'))['rating__max'] ##TODO:probar bien
            day = max_date.day
            month = max_date.month
            year = max_date.year
            if day == calendar.monthrange(year, month): ##Si es el ultimo dia del mes
                from_date = dt.date(year=year if month < 12 else year+1, month=month+1 if month < 12 else 1, day=1)
            else:
                from_date = dt.date(year=year, month=month, day=day+1)
        return from_date

    def get_to_date(self, fromDate):
        """
        Devuelve el máximo día del mes en el cual una agenda debe ser creada.
        :param fromDate:
        :return:
        """
        month = fromDate.month
        year = fromDate.year
        maxday = calendar.monthrange(year, month)[1]
        return dt.date(year=year, month=month, day=maxday)

    def validate(self, attrs):
        profesional = attrs['profesional']
        prestacion = attrs['prestacion']

        if not prestacion in profesional.prestaciones.all():
            raise serializers.ValidationError({'Prestacion': _('La prestacion no coincide con el profesional')})
        return attrs

    @transaction.atomic
    def create(self, validated_data):
        """
        Crea una nueva agenda
        POST /agendas
        """
        reversion.set_user(self._context['request'].user)

        profesional = validated_data.pop('profesional')
        prestacion = validated_data.pop('prestacion')
        validFrom = validated_data.get('validFrom')
        validFrom = validFrom if validFrom is not None else self.get_from_date(profesional, prestacion)
        validTo = validated_data.get('validTo')
        validTo = validTo if validTo is not None else self.get_to_date(validFrom)

        instance = Agenda.objects.create(
            status=validated_data.get('status'),
            start=validated_data.get('start'),          #Hora inicio de turnos
            end=validated_data.get('end'),              #Hora fin de turnos
            validFrom=validFrom,                        #Fecha desde la cual se debe crear la agenda
            validTo=validTo,                            #Fecha hasta la cual se debe crear la agenda
            profesional=profesional,             #Profesional para el cual se desea crear una agenda
            prestacion=prestacion                 #Prestación para la cual se desea crear una agenda
        )
        periods = validated_data.pop('periods')
        # Agrego datos de la revision
        reversion.set_user(self._context['request'].user)
        reversion.set_comment("Created agenda")

        return self.load_agenda(periods, instance)

    def load_agenda(self, periods, agenda_instance):
        """
        Procesa los periodos de una agenda y guarda la entidad completa
        """

        for period in periods:
            period_instance = Period.objects.create(
                start=period.get('start'),
                end=period.get('end'),
                selected=period.get('selected'),
                agenda=agenda_instance
            )
            period_instance.save()

            days_of_week = period.pop('daysOfWeek')

            for day_of_week in days_of_week:
                day_of_week_instance = DayOfWeek.objects.create(
                    index=day_of_week.index,
                    name=day_of_week.name,
                    selected=day_of_week.selected,
                    period=period_instance
                )
                day_of_week_instance.save()

                self.insert_period_days(agenda_instance, period_instance, day_of_week_instance)
        agenda_instance.save()
        return agenda_instance

    def insert_period_days(self, agenda, period, day_of_week):
        """
        Crea los turnoSlots para un perido de una agenda y un weekday en particular
        Toma en cuenta las ausencias del profesional y la colision con turnos
        ya tomados del profesional
        """

        start_date = agenda.validFrom
        end_date = agenda.validTo

        total_days = (end_date - start_date).days + 1

        for day_number in range(total_days):
            #Por cada dia dentro de la agenda
            current_date = (start_date + dt.timedelta(days=day_number))
            if current_date.weekday() == day_of_week.index:
                #Si el dia que recorro corresponde con el dia de la semana que estoy procesando
                if day_of_week.selected is True:
                    # Chequeo si no existe un turnoSlot dado de baja para ese periodo y dia
                    turno_slots = TurnoSlot.objects.filter(agenda=agenda,
                                                           start=period.start,
                                                           end=period.end,
                                                           day=current_date,
                                                           state=TurnoSlot.STATE_DELETED
                                                          )
                    if turno_slots:
                        turnoSlot_service.activate_turno_slot(turno_slots[0])
                    else:
                        # Creo el turno
                        turnoSlot_service.create_turno_slot(current_date,
                                                            period.start,
                                                            period.end,
                                                            agenda,
                                                            agenda.profesional,
                                                            agenda.prestacion)


    @transaction.atomic
    def update(self, instance, validated_data):
        """
        Modifica el estado o los periodos de una agenda
        PUT /agendas/id
        """

        #No permitir modificar datos de la agenda
        # profesional = validated_data.pop('profesional')
        # prestacion = validated_data.pop('prestacion')
        # instance.start = validated_data.get('start', instance.start)
        # instance.end = validated_data.get('end', instance.end)
        # instance.validFrom = validated_data.get('validFrom', instance.validFrom)
        # instance.validTo = validated_data.get('validTo', instance.validTo)

        if validated_data.get('status') is not None and validated_data.get('status') != instance.status:
            if (instance.status == Agenda.STATUS_ACTIVE and
                    validated_data.get('status') == Agenda.STATUS_INACTIVE):
                #Desactivo agenda
                self.deactivate(instance)
            elif (instance.status == Agenda.STATUS_INACTIVE and
                  validated_data.get('status') == Agenda.STATUS_ACTIVE):
                #Activo agenda
                self.activate(instance)

        periodos = self._context['request']._data['periods']
        return self.load_updated_agenda(instance, periodos)

    def load_updated_agenda(self, agenda_instance, periods):
        """
        Procesa la modificacion de periodos de una agenda y guarda la entidad completa
        """
        # Activo guardado de version de objetos
        with reversion.create_revision(atomic=True):
            for period in periods:
                days_of_week = period.pop('daysOfWeek')
                for day_of_week in days_of_week:
                    # Busco el estado actual del day_of_week
                    instance_day_of_week = DayOfWeek.objects.get(pk=day_of_week["id"])
                    if day_of_week["selected"] is True and instance_day_of_week.selected is False:
                    # Si cambia a seleccionado
                    # Guardo el cambio y creo
                    # los turnos para el day_of_week
                        instance_day_of_week.selected = True
                        instance_day_of_week.save()
                        current_period = Period(**period)
                        current_period.start = datetime.strptime(current_period.start, '%H:%M:%S')
                        current_period.end = datetime.strptime(current_period.end, '%H:%M:%S')
                        self.insert_period_days(agenda_instance,
                                                current_period,
                                                instance_day_of_week)

                    if day_of_week["selected"] is False and instance_day_of_week.selected is True:
                    # Si cambia a no seleccionado
                    # Guardo el cambio y cancelo
                    # los turnos para el day_of_week
                        instance_day_of_week.selected = False
                        instance_day_of_week.save()
                        current_period = Period(**period)
                        self.disable_period_days(agenda_instance,
                                                 current_period,
                                                 instance_day_of_week)

            # Guardo la agenda
            agenda_instance.save()
            # Agrego datos de la revision
            reversion.set_user(self._context['request'].user)
            reversion.set_comment("Modified agenda")
        return agenda_instance

    def activate(self, instance):
        """
        Activa una agenda. Limpia sus turnos y los activa.
        """

        if instance.profesional.status == Agenda.STATUS_INACTIVE:
            raise FailedDependencyException('El profesional de la agenda debe estar activo')

        instance.status = Agenda.STATUS_ACTIVE
        days_of_week = DayOfWeek.objects.filter(period__agenda=instance)

        if instance.validFrom > dt.date.today():
            start_date = instance.validFrom
        else:
            start_date = dt.date.today()

        end_date = instance.validTo

        total_days = (end_date - start_date).days + 1

        for day_of_week in days_of_week:
            for day_number in range(total_days):
                #Por cada dia dentro de la agenda
                current_date = (start_date + dt.timedelta(days=day_number))
                if current_date.weekday() == day_of_week.index:
                    #Si el dia que recorro corresponde con el dia de la semana que estoy procesando
                    if day_of_week.selected is True:
                        # Chequeo si no existe un turnoSlot dado de baja para ese periodo y dia
                        turno_slot = TurnoSlot.objects.get(agenda=instance,
                                                           start=day_of_week.period.start,
                                                           end=day_of_week.period.end,
                                                           day=current_date,
                                                           state=TurnoSlot.STATE_DELETED
                                                          )
                        turnoSlot_service.activate_turno_slot(turno_slot)
        instance.save()
        # Agrego datos de la revision
        reversion.set_user(self._context['request'].user)
        reversion.set_comment("Activated agenda")


    def deactivate(self, instance):
        """
        Desactiva una agenda y todos sus turnos.
        """
        turno_slots = TurnoSlot.objects.filter(agenda=instance,
                                               status=TurnoSlot.STATUS_ACTIVE,
                                               state__in=[TurnoSlot.STATE_AVAILABLE,
                                                          TurnoSlot.STATE_OCCUPIED,
                                                          TurnoSlot.STATE_CONFLICT],
                                               day__gte=dt.date.today())
        for turno_slot in turno_slots:
            turnoSlot_service.delete_turno_slot(turno_slot)
        instance.status = Agenda.STATUS_INACTIVE
        instance.save()
        # Agrego datos de la revision
        reversion.set_user(self._context['request'].user)
        reversion.set_comment("Deactivated agenda")


    def disable_period_days(self, agenda, period, day_of_week):
        """
        Elimina todos los turnos de una agenda que correspondan
        a un periodo y un day_of_week
        """

        # Cuento los dias a recorrer
        total_days = (agenda.validTo - agenda.validFrom).days + 1

        # Recorro la duracion de la agenda
        for day_number in range(total_days):
            current_date = (agenda.validFrom + dt.timedelta(days=day_number))
            # Si el dia corresponde con el que estoy trabajando
            if current_date.weekday() == day_of_week.index:
                turno_slots = TurnoSlot.objects.filter(agenda=agenda,
                                                       start=period.start,
                                                       end=period.end,
                                                       day=current_date,
                                                       state__in=[TurnoSlot.STATE_AVAILABLE,
                                                                  TurnoSlot.STATE_OCCUPIED,
                                                                  TurnoSlot.STATE_CONFLICT])
                for turno_slot in turno_slots:
                    turnoSlot_service.delete_turno_slot(turno_slot)

    class Meta:
        model = Agenda
        fields = ('id', 'status', 'start', 'end', 'validFrom', 'validTo', 'periods', 'profesional', 'prestacion')
