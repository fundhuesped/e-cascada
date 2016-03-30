#!/usr/bin/python
# -*- coding: utf-8 -*-

from rest_framework import serializers
from hc_common.models import DocumentType, SexType, Location, CivilStatusType, EducationType, SocialService
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

    location = serializers.HyperlinkedRelatedField(
        view_name="hc_common:Location-detail",
        queryset=Location.objects
    )

    civilStatus = serializers.HyperlinkedRelatedField(
        view_name="hc_common:CivilStatusType-detail",
        queryset=CivilStatusType.objects
    )

    education = serializers.HyperlinkedRelatedField(
        view_name="hc_common:EducationType-detail",
        queryset=EducationType.objects
    )

    socialService = serializers.HyperlinkedRelatedField(
        view_name="hc_common:SocialService-detail",
        queryset=SocialService.objects
    )

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
        fields = ('id', 'idpaciente', 'firstName', 'otherNames', 'fatherSurname', 'motherSurname', 'birthDate', 'email',
                  'telephone',
                  'street', 'postal', 'status', 'documentType', 'documentNumber', 'genderAtBirth',
                  'genderOfChoice', 'location', 'primaryPhoneNumber', 'primaryPhoneContact', 'primaryPhoneMessage',
                  'occupation', 'civilStatus', 'education', 'socialService', 'socialServiceNumber', 'terms')
