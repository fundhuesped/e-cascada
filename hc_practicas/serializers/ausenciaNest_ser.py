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

    start = serializers.TimeField(
        default = datetime.time(0,0,0)
    )
    end = serializers.TimeField(
        default = datetime.time(23,59,59)
    )

    def create(self, validated_data):
        profesional = validated_data.pop('profesional')
        instance = Ausencia.objects.create(
            day=validated_data.get('day'),
            start=validated_data.get('start'),
            end=validated_data.get('end'),
            profesional=profesional
        )
        #Cuando se crea una ausencia, inhabilita todos los turnos del profesional asociado
        turnos = Turno.objects.filter(day=instance.day, profesional=instance.profesional)
        for turno in turnos:
            if (turno.start >= instance.start and turno.start <= instance.end) or (
                    turno.end <= instance.end and turno.end >= instance.start):
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
        fields = ('id', 'day', 'start', 'end', 'profesional', 'status')
