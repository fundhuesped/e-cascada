#!/usr/bin/python
# -*- coding: utf-8 -*-

from rest_framework import serializers
from hc_common.models import Persona
from hc_common.serializers import DocumentTypeNestSerializer, SexTypeNestSerializer, PhoneNestSerializer, \
    AddressNestSerializer, CivilStatusTypeNestSerializer, SocialServiceNestSerializer, \
    EducationTypeNestSerializer


class PersonaNestSerializer(serializers.ModelSerializer):
    """
    Serializa una Persona
    """
    id = serializers.ReadOnlyField()

    documentType = DocumentTypeNestSerializer(
        many=False
    )

    genderAtBirth = SexTypeNestSerializer(
        many=False
    )

    genderOfChoice = SexTypeNestSerializer(
        many=False
    )

    telephones = PhoneNestSerializer(
        many=True
    )

    address = AddressNestSerializer(
        many=False
    )

    civilStatus = CivilStatusTypeNestSerializer(
        many=False
    )

    socialService = SocialServiceNestSerializer(
        many=False
    )

    education = EducationTypeNestSerializer(
        many=False
    )

    def create(self, validated_data):
        documentType = validated_data.pop('documentType')
        genderAtBirth = validated_data.pop('genderAtBirth')
        genderOfChoice = validated_data.pop('genderOfChoice')
        telephones = validated_data.pop('telephones')
        address = validated_data.pop('address')
        civilStatus = validated_data.pop('civilStatus')
        socialService = validated_data.pop('socialService')
        education = validated_data.pop('education')
        persona = Persona.objects.create(
            firstName=validated_data.get('firstName'),
            otherNames=validated_data.get('otherNames'),
            fatherSurname=validated_data.get('fatherSurname'),
            motherSurname=validated_data.get('motherSurname'),
            birthDate=validated_data.get('birthDate'),
            documentNumber=validated_data.get('documentNumber'),
            email=validated_data.get('email'),
            occupation=validated_data.get('occupation'),
            socialNumber=validated_data.get('socialNumber'),
            terms=validated_data.get('terms'),
            status='Active',
            documentType=documentType,
            genderAtBirth=genderAtBirth,
            genderOfChoice=genderOfChoice,
            telephones=telephones,
            address=address,
            civilStatus=civilStatus,
            socialService=socialService,
            education=education
        )
        return persona

    def update(self, instance, validated_data):
        documentType = validated_data.pop('documentType')
        genderAtBirth = validated_data.pop('genderAtBirth')
        genderOfChoice = validated_data.pop('genderOfChoice')
        telephones = validated_data.pop('telephones')
        address = validated_data.pop('address')
        civilStatus = validated_data.pop('civilStatus')
        socialService = validated_data.pop('socialService')
        education = validated_data.pop('education')
        instance.firstName = validated_data.get('firstName', instance.firstName)
        instance.otherNames = validated_data.get('otherNames', instance.otherNames)
        instance.fatherSurname = validated_data.get('fatherSurname', instance.fatherSurname)
        instance.motherSurname = validated_data.get('motherSurname', instance.motherSurname)
        instance.birthDate = validated_data.get('birthDate', instance.birthDate)
        instance.documentNumber = validated_data.get('documentNumber', instance.documentNumber)
        instance.email = validated_data.get('email', instance.email)
        instance.status = validated_data.get('status', instance.status)
        instance.documentType = documentType
        instance.genderAtBirth = genderAtBirth
        instance.genderOfChoice = genderOfChoice
        instance.telephones = telephones
        instance.address = address
        instance.civilStatus = civilStatus
        instance.socialService = socialService
        instance.education = education
        instance.save()

        return instance

    class Meta:
        model = Persona
        fields = (
        'id', 'status', 'firstName', 'otherNames', 'fatherSurname', 'motherSurname', 'birthDate', 'email', 'occupation',
        'socialNumber', 'terms', 'telephones', 'address', 'civilStatus', 'socialService', 'education', 'documentType',
        'documentNumber', 'genderAtBirth', 'genderOfChoice')
