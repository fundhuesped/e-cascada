#!/usr/bin/python
# -*- coding: utf-8 -*-

from rest_framework import serializers
import datetime
from hc_practicas.models import Turno, Ausencia
from hc_practicas.serializers import ProfesionalNestedSerializer, PrestacionNestedSerializer


class AusenciaNestSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.ReadOnlyField()

    profesional = ProfesionalNestedSerializer(
        many=False
    )

    def create(self, validated_data):
        profesional = validated_data.pop('profesional')
        instance = Ausencia.objects.create(
            start_day=validated_data.get('start_day'),
            end_day=validated_data.get('end_day'),
            profesional=profesional,
            notes = validated_data.get('notes'),
            reason = validated_data.get('reason')
        )

        #Cuando se crea una ausencia, inhabilita todos los turnos del profesional asociado
        turnos = Turno.objects.filter(day__range=[instance.start_day, instance.end_day], profesional=instance.profesional)
        for turno in turnos:
            turno.status = Turno.STATUS_INACTIVE
            turno.save()

        return instance

    #Método agregado por compatibilidad. Las ausencias solo se pueden agregar o eliminar
    def update(self, instance, validated_data):
        profesional = validated_data.pop('profesional')
        instance.day = validated_data.get('day', instance.day)
        instance.start = validated_data.get('start', instance.start)
        instance.end = validated_data.get('end', instance.end)
        instance.profesional = profesional
        instance.save()

        return instance



    class Meta:
        model = Ausencia
        fields = ('id', 'start_day', 'end_day', 'profesional', 'status', 'reason','notes')
