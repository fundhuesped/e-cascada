#!/usr/bin/python
# -*- coding: utf-8 -*-

from rest_framework import serializers
from hc_practicas.models import Agenda, Period, DayOfWeek, Profesional, Prestacion, Turno
from hc_practicas.serializers import PeriodNestSerializer, ProfesionalNestSerializer, PrestacionNestSerializer
import datetime as dt


class AgendaNestSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.ReadOnlyField()

    periods = PeriodNestSerializer(
        many=True
    )

    profesional = ProfesionalNestSerializer(
        many=False
    )

    prestacion = PrestacionNestSerializer(
        many=False
    )

    def create(self, validated_data):
        profesional = validated_data.pop('profesional')
        profesional = Profesional.objects.filter(pk=profesional['id'])
        prestacion = validated_data.pop('prestacion')
        prestacion = Prestacion.objects.filter(pk=prestacion['id'])
        instance = Agenda.objects.create(
            status=validated_data.get('status'),
            start=validated_data.get('start'),
            end=validated_data.get('end'),
            validFrom=validated_data.get('validFrom'),
            validTo=validated_data.get('validTo'),
            profesional=profesional[0],
            prestacion=prestacion[0]
        )

        periods = validated_data.pop('periods')

        return self.load_agenda(periods, instance, profesional[0], prestacion[0])

    def update(self, instance, validated_data):
        profesional = validated_data.pop('profesional')
        profesional = Profesional.objects.filter(pk=profesional['id'])
        prestacion = validated_data.pop('prestacion')
        prestacion = Prestacion.objects.filter(pk=prestacion['id'])
        instance.status = validated_data.get('status', instance.status)
        instance.start = validated_data.get('start', instance.start)
        instance.end = validated_data.get('end', instance.end)
        instance.validFrom = validated_data.get('validFrom', instance.validFrom)
        instance.validTo = validated_data.get('validTo', instance.validTo)
        instance.profesional = profesional[0]
        instance.prestacion = prestacion[0]

        for period in instance.periods.all():
            for dayOfWeek in period.daysOfWeek.all():
                dayOfWeek.delete()
            period.delete()

        instance.periods.clear()
        periods = validated_data.pop('periods')

        return self.load_agenda(periods, instance, profesional[0], prestacion[0])

    def load_agenda(self, periods, agenda_instance, profesional, prestacion):
        for period in periods:
            period_instance = Period.objects.create(
                start=period.get('start'),
                end=period.get('end'),
                selected=period.get('selected')
            )

            days_of_week = period.pop('daysOfWeek')
            for dayOfWeek in days_of_week:
                day_instance = DayOfWeek.objects.create(
                    index=dayOfWeek.get('index'),
                    name=dayOfWeek.get('name'),
                    selected=dayOfWeek.get('selected')
                )
                day_instance.save()
                period_instance.daysOfWeek.add(day_instance)
                self.insert_period_days(agenda_instance, period_instance, day_instance, profesional, prestacion)

            period_instance.save()
            agenda_instance.periods.add(period_instance)

        return agenda_instance

    def insert_period_days(self, agenda, period, dayOfWeek, profesional, prestacion):
        start_date = agenda.validFrom
        end_date = agenda.validTo

        total_days = (end_date - start_date).days + 1

        for day_number in range(total_days):
            current_date = (start_date + dt.timedelta(days=day_number))
            if current_date.weekday() == dayOfWeek.index:
                turno_instance = Turno.objects.create(
                    day=current_date,
                    start=period.start,
                    end=period.end,
                    profesional=profesional,
                    prestacion=prestacion
                )
                turno_instance.save()

    class Meta:
        model = Agenda
        fields = ('id', 'status', 'start', 'end', 'validFrom', 'validTo', 'periods', 'profesional', 'prestacion')
