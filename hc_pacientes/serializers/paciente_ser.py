#!/usr/bin/python
# -*- coding: utf-8 -*-

from rest_framework import serializers
from hc_common.models import DocumentType, SexType
from hc_pacientes.models import Paciente

class PacienteSerializer(serializers.HyperlinkedModelSerializer):
    """
    Serializa un Paciente
    """
    id = serializers.ReadOnlyField()

    documentType = serializers.HyperlinkedRelatedField(
        view_name="hc_common:DocumentType-detail",
        queryset=DocumentType.objects
    )

    genderAtBirth = serializers.HyperlinkedRelatedField(
        view_name="hc_common:SexType-detail",
        queryset=SexType.objects
    )

    genderOfChoice = serializers.HyperlinkedRelatedField(
        view_name="hc_common:SexType-detail",
        queryset=SexType.objects
    )

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
        persona = Paciente.objects.create(**validated_data)
        return persona

    class Meta:
        model = Paciente
        fields = ('id', 'firstName', 'otherNames', 'fatherSurname', 'motherSurname', 'birthDate', 'email', 'telephone', 'meta', 'documentType', 'documentNumber', 'genderAtBirth', 'genderOfChoice')
