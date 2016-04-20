#!/usr/bin/python
# -*- coding: utf-8 -*-

from rest_framework import serializers
from hc_practicas.models import Profesional, Prestacion, Turno
from hc_pacientes.models import Paciente
from hc_pacientes.serializers import PacienteNestSerializer
from hc_practicas.serializers import ProfesionalNestSerializer, PrestacionNestSerializer


class TurnoNestSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.ReadOnlyField()

    paciente = PacienteNestSerializer(
        many=False
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
        paciente = validated_data.pop('paciente')
        paciente = Paciente.objects.filter(pk=paciente['id'])
        instance = Turno.objects.create(
            day=validated_data.get('day'),
            start=validated_data.get('start'),
            end=validated_data.get('end'),
            taken=validated_data.get('taken'),
            profesional=profesional[0],
            prestacion=prestacion[0],
            paciente=paciente[0]
        )

        return instance

    def update(self, instance, validated_data):
        profesional = validated_data.pop('profesional')
        profesional = Profesional.objects.filter(pk=profesional['id'])
        prestacion = validated_data.pop('prestacion')
        prestacion = Prestacion.objects.filter(pk=prestacion['id'])
        paciente = validated_data.pop('paciente')
        paciente = Paciente.objects.filter(pk=paciente['id'])
        instance.day = validated_data.get('day', instance.day)
        instance.start = validated_data.get('start', instance.start)
        instance.end = validated_data.get('end', instance.end)
        instance.taken = validated_data.get('taken', instance.taken)
        instance.profesional = profesional[0]
        instance.prestacion = prestacion[0]
        instance.paciente = paciente[0]

        instance.save()

        return instance

    class Meta:
        model = Turno
        fields = ('id', 'day', 'start', 'end', 'taken', 'paciente', 'profesional', 'prestacion')
