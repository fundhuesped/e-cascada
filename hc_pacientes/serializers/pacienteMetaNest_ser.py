#!/usr/bin/python
# -*- coding: utf-8 -*-

from rest_framework import serializers
from hc_pacientes.models import Paciente, PacienteMeta
from hc_pacientes.serializers import PacienteNestedSerializer

class PacienteMetaNestSerializer(serializers.ModelSerializer):
    """
    Serializa un Meta Paciente
    """
    id = serializers.ReadOnlyField()

    paciente = PacienteNestedSerializer(
        many=False
    )

    def create(self, validated_data):
        paciente = validated_data.pop('paciente')
        meta = PacienteMeta.objects.create(
            metaType = validated_data.get('metaType'),
            metaValue = validated_data.get('metaValue'),
            paciente = paciente
        )

        return meta

    def update(self, instance, validated_data):
        paciente = validated_data.pop('paciente')
        instance.metaType= validated_data.get('metaType', instance.metaType)
        instance.metaValue = validated_data.get('metaValue', instance.metaValue)
        instance.paciente = paciente
        instance.save()

        return instance


    class Meta:
        model = PacienteMeta
        fields = ('id', 'metaType', 'metaValue', 'paciente')