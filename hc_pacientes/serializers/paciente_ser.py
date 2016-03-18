#!/usr/bin/python
# -*- coding: utf-8 -*-

from rest_framework import serializers
from hc_pacientes.models import Paciente

class PacienteSerializer(serializers.HyperlinkedModelSerializer):
    """
    Serializa un Paciente
    """
    id = serializers.ReadOnlyField()
    documento = serializers.HyperlinkedRelatedField( #elemento read only, para relacionarlo con el documento
        read_only=True,
        view_name='hc_common:Documento-detail')

    meta = serializers.HyperlinkedRelatedField( #elemento read only, para relacionarlo con el meta del paciente
        read_only=True,
        many=True,
        view_name='hc_pacientes:PacienteMeta-detail')

    def create(self, validated_data):
        """
        Crea un paciente
        :param validated_data: Valores con los cuales crear el Paciente
        :return: Una nueva instancia de Paciente
        """
        persona =  Paciente.objects.create(**validated_data)
        return persona


    class Meta:
        model = Paciente
        fields = ('id', 'firstName', 'otherNames', 'fatherSurname', 'motherSurname', 'documento', 'birthDate', 'idpaciente', 'meta')