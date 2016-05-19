#!/usr/bin/python
# -*- coding: utf-8 -*-

from rest_framework import serializers
from hc_practicas.models import Profesional, Prestacion, Turno
from hc_pacientes.models import Paciente
from hc_pacientes.serializers import PacienteNestedSerializer
from hc_practicas.serializers import ProfesionalNestedSerializer, PrestacionNestedSerializer


class TurnoNestSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.ReadOnlyField()

    paciente = PacienteNestedSerializer(
        many=False
    )

    profesional = ProfesionalNestedSerializer(
        many=False
    )

    prestacion = PrestacionNestedSerializer(
        many=False
    )

    def create(self, validated_data):
        profesional = validated_data.pop('profesional')
        prestacion = validated_data.pop('prestacion')
        paciente = validated_data.pop('paciente')
        instance = Turno.objects.create(
            day=validated_data.get('day'),
            start=validated_data.get('start'),
            end=validated_data.get('end'),
            taken=validated_data.get('taken'),
            profesional=profesional,
            prestacion=prestacion,
            paciente=paciente
        )

        return instance

    def update(self, instance, validated_data):
        profesional = validated_data.pop('profesional')
        prestacion = validated_data.pop('prestacion')
        paciente = validated_data.pop('paciente')
        instance.day = validated_data.get('day', instance.day)
        instance.start = validated_data.get('start', instance.start)
        instance.end = validated_data.get('end', instance.end)
        instance.taken = validated_data.get('taken', instance.taken)
        instance.profesional = profesional
        instance.prestacion = prestacion
        instance.paciente = paciente

        instance.save()

        return instance

    class Meta:
        model = Turno
        fields = ('id', 'day', 'start', 'end', 'taken', 'paciente', 'profesional', 'prestacion', 'status')
