#!/usr/bin/python
# -*- coding: utf-8 -*-

from rest_framework import serializers
from hc_practicas.models import Agenda, Period, DayOfWeek, Profesional, Prestacion
from hc_practicas.serializers import PeriodNestSerializer, ProfesionalNestSerializer, PrestacionNestSerializer


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
        print prestacion
        agenda_instance = Agenda.objects.create(
            start=validated_data.get('start'),
            end=validated_data.get('end'),
            validFrom=validated_data.get('validFrom'),
            validTo=validated_data.get('validTo'),
            profesional=profesional[0],
            prestacion=prestacion[0]
        )

        periods = validated_data.pop('periods')
        for period in periods:
            period_instance = Period.objects.create(
                start=period.get('start'),
                end=period.get('end'),
                selected=period.get('selected')
            )

            days_of_week = period.pop('daysOfWeek')
            for dayOfWeek in days_of_week:
                day_instance = DayOfWeek.objects.create(
                    name=dayOfWeek.get('name'),
                    selected=dayOfWeek.get('selected')
                )
                day_instance.save()
                period_instance.daysOfWeek.add(day_instance)

            period_instance.save()
            agenda_instance.periods.add(period_instance)

        agenda_instance.save()

        return agenda_instance

    class Meta:
        model = Agenda
        fields = ('id', 'start', 'end', 'validFrom', 'validTo', 'periods', 'profesional', 'prestacion')
