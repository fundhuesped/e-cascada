#!/usr/bin/python
# -*- coding: utf-8 -*-

from rest_framework import serializers
from hc_common.models import DocumentType, SexType, Phone, Address, CivilStatusType, SocialService, EducationType
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

    telephones = serializers.HyperlinkedRelatedField(
        view_name="hc_common:Phone-detail",
        queryset=Phone.objects
    )

    address = serializers.HyperlinkedRelatedField(
        view_name="hc_common:Address-detail",
        queryset=Address.objects
    )

    civilStatus = serializers.HyperlinkedRelatedField(
        view_name="hc_common:CivilStatusType-detail",
        queryset=CivilStatusType.objects
    )

    socialService = serializers.HyperlinkedRelatedField(
        view_name="hc_common:SocialService-detail",
        queryset=SocialService.objects
    )

    education = serializers.HyperlinkedRelatedField(
        view_name="hc_common:EducationType-detail",
        queryset=EducationType.objects
    )

    meta = serializers.HyperlinkedRelatedField(
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
        fields = ('id', 'firstName', 'otherNames', 'fatherSurname', 'motherSurname', 'birthDate', 'email', 'occupation',
                  'telephones', 'meta', 'address', 'civilStatus', 'socialService', 'socialNumber', 'education', 'terms',
                  'status', 'documentType', 'documentNumber', 'genderAtBirth', 'genderOfChoice')
