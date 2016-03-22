#!/usr/bin/python
# -*- coding: utf-8 -*-

from rest_framework import serializers
from hc_pacientes.models import Paciente, PacienteMeta
from hc_pacientes.serializers import PacienteMetaNestedSerializer

class PacienteNestSerializer(serializers.ModelSerializer):
    """
    Serializa una Paciente
    """
    id = serializers.ReadOnlyField()

    meta = PacienteMetaNestedSerializer(
        many=True,
        read_only=True
    )

    def create(self, validated_data):
        paciente = Paciente.objects.create(**validated_data)
        return paciente

    def update(self, instance, validated_data):
        instance.firstName= validated_data.get('firstName', instance.firstName)
        instance.otherNames = validated_data.get('otherNames', instance.otherNames)
        instance.fatherSurname = validated_data.get('fatherSurname', instance.fatherSurname)
        instance.motherSurname = validated_data.get('motherSurname', instance.motherSurname)
        instance.birthDate = validated_data.get('birthDate', instance.birthDate)
        instance.idpaciente = validated_data.get('idpaciente', instance.idpaciente)
        instance.save()

        return instance


    class Meta:
        model = Paciente
        fields = ('id', 'firstName', 'otherNames', 'fatherSurname', 'motherSurname', 'birthDate', 'idpaciente', 'meta')