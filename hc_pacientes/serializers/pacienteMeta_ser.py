#!/usr/bin/python
# -*- coding: utf-8 -*-

from rest_framework import serializers
from hc_pacientes.models import Paciente, PacienteMeta

class PacienteMetaSerializer(serializers.HyperlinkedModelSerializer):
    """
    Serializa un Paciente
    """
    id = serializers.ReadOnlyField()
    paciente = serializers.HyperlinkedRelatedField( #elemento relacionado con el paciente
        view_name='hc_pacientes:Paciente-detail',
        queryset=Paciente.objects)


    def create(self, validated_data):
        """
        Crea un Metapaciente
        :param validated_data: Valores con los cuales crear el MetaPaciente
        :return: Una nueva instancia de Paciente
        """
        paciente =  PacienteMeta.objects.create(**validated_data)
        return paciente


    class Meta:
        model = PacienteMeta
        fields = ('id', 'metaType', 'metaValue', 'paciente')