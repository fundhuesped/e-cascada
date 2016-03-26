#!/usr/bin/python
# -*- coding: utf-8 -*-

from rest_framework import serializers
from hc_pacientes.models import Paciente
from hc_pacientes.serializers import PacienteMetaNestedSerializer
from hc_common.serializers import DocumentTypeNestedSerializer, SexTypeNestedSerializer

class PacienteNestSerializer(serializers.ModelSerializer):
    """
    Serializa una Paciente
    """
    id = serializers.ReadOnlyField()

    meta = PacienteMetaNestedSerializer(
        many=True,
        read_only=True
    )

    documentType = DocumentTypeNestedSerializer(
        many=False
    )

    genderAtBirth = SexTypeNestedSerializer(
        many=False
    )

    genderOfChoice = SexTypeNestedSerializer(
        many=False
    )

    def create(self, validated_data):
        documentType = validated_data.pop('documentType')
        genderAtBirth = validated_data.pop('genderAtBirth')
        genderOfChoice = validated_data.pop('genderOfChoice')
        paciente = Paciente.objects.create(
            idpaciente = validated_data.get('idpaciente'),
            firstName = validated_data.get('firstName'),
            otherNames = validated_data.get('otherNames'),
            fatherSurname = validated_data.get('fatherSurname'),
            motherSurname = validated_data.get('motherSurname'),
            birthDate = validated_data.get('birthDate'),
            documentNumber = validated_data.get('documentNumber'),
            email = validated_data.get('email'),
            telephone = validated_data.get('telephone'),
            status = validated_data.get('status'),
            documentType = documentType,
            genderAtBirth = genderAtBirth,
            genderOfChoice = genderOfChoice
        )
        return paciente

    def update(self, instance, validated_data):
        documentType = validated_data.pop('documentType')
        genderAtBirth = validated_data.pop('genderAtBirth')
        genderOfChoice = validated_data.pop('genderOfChoice')
        instance.idpaciente = validated_data.get('idpaciente', instance.idpaciente)
        instance.firstName = validated_data.get('firstName', instance.firstName)
        instance.otherNames = validated_data.get('otherNames', instance.otherNames)
        instance.fatherSurname = validated_data.get('fatherSurname', instance.fatherSurname)
        instance.motherSurname = validated_data.get('motherSurname', instance.motherSurname)
        instance.birthDate = validated_data.get('birthDate', instance.birthDate)
        instance.documentNumber = validated_data.get('documentNumber', instance.documentNumber)
        instance.email = validated_data.get('email', instance.email)
        instance.telephone = validated_data.get('telephone', instance.telephone)
        instance.status = validated_data.get('status', instance.status)
        instance.documentType = documentType
        instance.genderAtBirth = genderAtBirth
        instance.genderOfChoice = genderOfChoice
        instance.save()

        return instance

    class Meta:
        model = Paciente
        fields = ('id', 'idpaciente', 'status', 'firstName', 'otherNames', 'fatherSurname', 'motherSurname', 'birthDate', 'email', 'telephone', 'meta', 'documentType', 'documentNumber', 'genderAtBirth', 'genderOfChoice')
