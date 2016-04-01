#!/usr/bin/python
# -*- coding: utf-8 -*-

from rest_framework import serializers
from hc_pacientes.models import Paciente
from hc_common.models import Location, Phone
from hc_common.serializers import DocumentTypeNestedSerializer, SexTypeNestedSerializer, LocationNestSerializer, \
    CivilStatusTypeNestedSerializer, SocialServiceNestedSerializer, EducationTypeNestedSerializer, PhoneNestSerializer


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

    location = LocationNestSerializer(
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

    primaryPhone = PhoneNestSerializer(
        many=False
    )

    secondPhone = PhoneNestSerializer(
        many=False
    )

    thirdPhone = PhoneNestSerializer(
        many=False
    )

    def create(self, validated_data):
        documentType = validated_data.pop('documentType')
        genderAtBirth = validated_data.pop('genderAtBirth')
        genderOfChoice = validated_data.pop('genderOfChoice')
        location = validated_data.pop('location')
        location = Location.objects.filter(pk=location['id'])
        civilStatus = validated_data.pop('civilStatus')
        education = validated_data.pop('education')
        socialService = validated_data.pop('socialService')
        primaryPhone = self.create_phone_instance(validated_data.pop('primaryPhone'))
        secondPhone = self.create_phone_instance(validated_data.pop('secondPhone'))
        thirdPhone = self.create_phone_instance(validated_data.pop('thirdPhone'))
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
            occupation=validated_data.get('occupation'),
            socialServiceNumber=validated_data.get('socialServiceNumber'),
            terms=validated_data.get('terms'),
            bornPlace=validated_data.get('bornPlace'),
            firstVisit=validated_data.get('firstVisit'),
            notes=validated_data.get('notes'),
            documentType=documentType,
            genderAtBirth=genderAtBirth,
            genderOfChoice=genderOfChoice,
            location=location[0],
            civilStatus=civilStatus,
            education=education,
            socialService=socialService,
            primaryPhone=primaryPhone,
            secondPhone=secondPhone,
            thirdPhone=thirdPhone
        )
        return paciente

    def create_phone_instance(self, phone):
        instance = Phone.objects.create(
            number=phone['number'],
            contact=phone['contact'],
            message=phone['message']
        )
        return instance

    def update(self, instance, validated_data):
        documentType = validated_data.pop('documentType')
        genderAtBirth = validated_data.pop('genderAtBirth')
        genderOfChoice = validated_data.pop('genderOfChoice')
        location = validated_data.pop('location')
        location = Location.objects.filter(pk=location['id'])
        civilStatus = validated_data.pop('civilStatus')
        education = validated_data.pop('education')
        socialService = validated_data.pop('socialService')
        primaryPhone = self.update_phone_instance(validated_data.pop('primaryPhone'))
        secondPhone = self.update_phone_instance(validated_data.pop('secondPhone'))
        thirdPhone = self.update_phone_instance(validated_data.pop('thirdPhone'))
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
        instance.occupation = validated_data.get('occupation', instance.occupation)
        instance.socialServiceNumber = validated_data.get('socialServiceNumber', instance.socialServiceNumber)
        instance.terms = validated_data.get('terms', instance.terms)
        instance.bornPlace = validated_data.get('bornPlace', instance.bornPlace)
        instance.firstVisit = validated_data.get('firstVisit', instance.firstVisit)
        instance.notes = validated_data.get('notes', instance.notes)
        instance.documentType = documentType
        instance.genderAtBirth = genderAtBirth
        instance.genderOfChoice = genderOfChoice
        instance.location = location[0]
        instance.civilStatus = civilStatus
        instance.education = education
        instance.socialService = socialService
        instance.primaryPhone = primaryPhone
        instance.secondPhone = secondPhone
        instance.thirdPhone = thirdPhone
        instance.save()

        return instance

    def update_phone_instance(self, phone):
        phones = Phone.objects.filter(pk=phone['id'])
        updated_phone = phones[0]
        updated_phone.number = phone['number']
        updated_phone.contact = phone['contact']
        updated_phone.message = phone['message']
        return updated_phone

    class Meta:
        model = Paciente
        fields = ('id', 'idpaciente', 'firstName', 'otherNames', 'fatherSurname', 'motherSurname', 'birthDate', 'email',
                  'street', 'postal', 'status', 'documentType', 'documentNumber', 'genderAtBirth',
                  'genderOfChoice', 'location', 'occupation', 'civilStatus', 'education', 'socialService',
                  'socialServiceNumber', 'terms', 'bornPlace', 'firstVisit', 'notes', 'primaryPhone', 'secondPhone',
                  'thirdPhone')
