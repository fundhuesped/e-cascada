#!/usr/bin/python
# -*- coding: utf-8 -*-

from rest_framework import serializers
from hc_common.models import Persona
from hc_common.serializers import DocumentTypeNestedSerializer, SexTypeNestedSerializer

class PersonaNestSerializer(serializers.ModelSerializer):
    """
    Serializa una Persona
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

    def create(self, validated_data):
        documentType = validated_data.pop('documentType')
        genderAtBirth = validated_data.pop('genderAtBirth')
        genderOfChoice = validated_data.pop('genderOfChoice')
        persona = Persona.objects.create(
            firstName = validated_data.get('firstName'),
            otherNames = validated_data.get('otherNames'),
            fatherSurname = validated_data.get('fatherSurname'),
            motherSurname = validated_data.get('motherSurname'),
            birthDate = validated_data.get('birthDate'),
            documentNumber = validated_data.get('documentNumber'),
            email = validated_data.get('email'),
            telephone = validated_data.get('telephone'),
            status = 'Active',
            documentType = documentType,
            genderAtBirth = genderAtBirth,
            genderOfChoice = genderOfChoice
        )
        return persona

    def update(self, instance, validated_data):
        documentType = validated_data.pop('documentType')
        genderAtBirth = validated_data.pop('genderAtBirth')
        genderOfChoice = validated_data.pop('genderOfChoice')
        instance.firstName= validated_data.get('firstName', instance.firstName)
        instance.otherNames = validated_data.get('otherNames', instance.otherNames)
        instance.fatherSurname = validated_data.get('fatherSurname', instance.fatherSurname)
        instance.motherSurname = validated_data.get('motherSurname', instance.motherSurname)
        instance.birthDate = validated_data.get('birthDate', instance.birthDate)
        instance.documentNumber = validated_data.get('documentNumber', instance.documentNumber)
        instance.email = validated_data.get('email', instance.email)
        instance.telephone = validated_data.get('telephone', instance.telephone)
        instance.status = validated_data.get('status', instance.status)
        instance.documetType = documentType
        instance.genderAtBirth = genderAtBirth
        instance.genderOfChoice = genderOfChoice
        instance.save()

        return instance

    class Meta:
        model = Persona
        fields = ('id', 'status', 'firstName', 'otherNames', 'fatherSurname', 'motherSurname', 'birthDate', 'email', 'telephone', 'documentType', 'documentNumber', 'genderAtBirth', 'genderOfChoice')