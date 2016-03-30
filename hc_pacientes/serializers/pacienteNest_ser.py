#!/usr/bin/python
# -*- coding: utf-8 -*-

from rest_framework import serializers
from hc_pacientes.models import Paciente
from hc_common.serializers import DocumentTypeNestedSerializer, SexTypeNestedSerializer, LocationNestedSerializer, \
    CivilStatusTypeNestedSerializer, SocialServiceNestedSerializer, EducationTypeNestedSerializer


class PacienteNestSerializer(serializers.ModelSerializer):
    """
    Serializa una Paciente
    """
    id = serializers.ReadOnlyField()

    documentType = DocumentTypeNestedSerializer(
        many=False
    )

    genderAtBirth = SexTypeNestedSerializer(
        many=False
    )

    genderOfChoice = SexTypeNestedSerializer(
        many=False
    )

    location = LocationNestedSerializer(
        many=False
    )

    civilStatus = CivilStatusTypeNestedSerializer(
        many=False, allow_null=True
    )

    education = EducationTypeNestedSerializer(
        many=False, allow_null=True
    )

    socialService = SocialServiceNestedSerializer(
        many=False, allow_null=True
    )

    def create(self, validated_data):
        documentType = validated_data.pop('documentType')
        genderAtBirth = validated_data.pop('genderAtBirth')
        genderOfChoice = validated_data.pop('genderOfChoice')
        location = validated_data.pop('location')
        civilStatus = validated_data.pop('civilStatus')
        education = validated_data.pop('education')
        socialService = validated_data.pop('socialService')
        paciente = Paciente.objects.create(
            idpaciente=validated_data.get('idpaciente'),
            firstName=validated_data.get('firstName'),
            otherNames=validated_data.get('otherNames'),
            fatherSurname=validated_data.get('fatherSurname'),
            motherSurname=validated_data.get('motherSurname'),
            birthDate=validated_data.get('birthDate'),
            documentNumber=validated_data.get('documentNumber'),
            email=validated_data.get('email'),
            street=validated_data.get('street'),
            postal=validated_data.get('postal'),
            status=validated_data.get('status'),
            primaryPhoneNumber=validated_data.get('primaryPhoneNumber'),
            primaryPhoneContact=validated_data.get('primaryPhoneContact'),
            primaryPhoneMessage=validated_data.get('primaryPhoneMessage'),
            occupation=validated_data.get('occupation'),
            socialServiceNumber=validated_data.get('socialServiceNumber'),
            terms=validated_data.get('terms'),
            documentType=documentType,
            genderAtBirth=genderAtBirth,
            genderOfChoice=genderOfChoice,
            location=location,
            civilStatus=civilStatus,
            education=education,
            socialService=socialService
        )
        return paciente

    def update(self, instance, validated_data):
        documentType = validated_data.pop('documentType')
        genderAtBirth = validated_data.pop('genderAtBirth')
        genderOfChoice = validated_data.pop('genderOfChoice')
        location = validated_data.pop('location')
        civilStatus = validated_data.pop('civilStatus')
        education = validated_data.pop('education')
        socialService = validated_data.pop('socialService')
        instance.idpaciente = validated_data.get('idpaciente', instance.idpaciente)
        instance.firstName = validated_data.get('firstName', instance.firstName)
        instance.otherNames = validated_data.get('otherNames', instance.otherNames)
        instance.fatherSurname = validated_data.get('fatherSurname', instance.fatherSurname)
        instance.motherSurname = validated_data.get('motherSurname', instance.motherSurname)
        instance.birthDate = validated_data.get('birthDate', instance.birthDate)
        instance.documentNumber = validated_data.get('documentNumber', instance.documentNumber)
        instance.email = validated_data.get('email', instance.email)
        instance.street = validated_data.get('street', instance.street)
        instance.postal = validated_data.get('postal', instance.postal)
        instance.status = validated_data.get('status', instance.status)
        instance.primaryPhoneNumber = validated_data.get('primaryPhoneNumber', instance.primaryPhoneNumber)
        instance.primaryPhoneContact = validated_data.get('primaryPhoneContact', instance.primaryPhoneContact)
        instance.primaryPhoneMessage = validated_data.get('primaryPhoneMessage', instance.primaryPhoneMessage)
        instance.occupation = validated_data.get('occupation', instance.occupation)
        instance.socialServiceNumber = validated_data.get('socialServiceNumber', instance.socialServiceNumber)
        instance.terms = validated_data.get('terms', instance.terms)
        instance.documentType = documentType
        instance.genderAtBirth = genderAtBirth
        instance.genderOfChoice = genderOfChoice
        instance.location = location
        instance.civilStatus = civilStatus
        instance.education = education
        instance.socialService = socialService
        instance.save()

        return instance

    class Meta:
        model = Paciente
        fields = ('id', 'idpaciente', 'firstName', 'otherNames', 'fatherSurname', 'motherSurname', 'birthDate', 'email',
                  'street', 'postal', 'status', 'documentType', 'documentNumber', 'genderAtBirth',
                  'genderOfChoice', 'location', 'primaryPhoneNumber', 'primaryPhoneContact', 'primaryPhoneMessage',
                  'occupation', 'civilStatus', 'education', 'socialService', 'socialServiceNumber', 'terms')
