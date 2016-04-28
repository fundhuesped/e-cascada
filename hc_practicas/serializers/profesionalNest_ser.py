#!/usr/bin/python
# -*- coding: utf-8 -*-

from rest_framework import serializers
from hc_common.models import Location
from hc_practicas.models import Profesional, Prestacion
from hc_practicas.serializers import PrestacionNestedSerializer
from hc_common.serializers import DocumentTypeNestedSerializer, SexTypeNestedSerializer, LocationNestedSerializer, \
    CivilStatusTypeNestedSerializer
from django.utils.translation import gettext as _


class ProfesionalNestSerializer(serializers.ModelSerializer):
    prestaciones = PrestacionNestedSerializer(
        many=True,
        read_only=False,
        allow_null=True,
        required=False
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

    location = LocationNestedSerializer(
        many=False
    )

    civilStatus = CivilStatusTypeNestedSerializer(
        many=False,
        allow_null=True,
        required=False
    )

    def validate(self, attrs):
        """
        Validaciones de datos básicos para el alta de un profesional
        :param attrs:
        :return:
        """
        if (not 'primaryPhoneNumber' in attrs) or attrs['primaryPhoneNumber'] is None:
            raise serializers.ValidationError({'primaryPhoneNumber': _('El teléfono primario es obligatorio para un profesional')})
        if (not 'primaryPhoneContact' in attrs) or attrs['primaryPhoneContact'] is None:
            raise serializers.ValidationError({'primaryPhoneContact': _('El teléfono primario es obligatorio para un profesional')})
        if (not 'primaryPhoneMessage' in attrs) or attrs['primaryPhoneMessage'] is None:
            raise serializers.ValidationError({'primaryPhoneMessage': _('El teléfono primario es obligatorio para un profesional')})
        if (not 'birthDate' in attrs) or attrs['birthDate'] is None:
           raise serializers.ValidationError({'birthDate': _('La fecha de nacimiento es obligatoria para un profesional')})
        if ((not 'documentNumber' in attrs) or attrs['documentNumber'] is None) or ((not 'documentType' in attrs) or attrs['documentType']) is None:
            raise serializers.ValidationError({'documentNumber': _('El tipo y número de documento son obligatorios')})
        if (not 'genderAtBirth' in attrs) or attrs['genderAtBirth'] is None:
            raise serializers.ValidationError({'genderAtBirth': _('El sexo al nacer es obligatorio')})
        if  (not 'genderOfChoice' in attrs) or attrs['genderOfChoice'] is None:
            raise serializers.ValidationError({'genderOfChoice': _('El sexo por elección es obligatorio')})
        if (not 'street' in attrs) or attrs['street'] is None:
            raise serializers.ValidationError({'street': _('El domicilio es obligatorio')})
        if (not 'postal' in attrs) or attrs['postal'] is None:
            raise serializers.ValidationError({'postal': _('El código postal es obligatorio')})
        if (not 'location' in attrs) or attrs['location'] is None:
            raise serializers.ValidationError({'location': _('La provincia, partido y localidad son obligatorios')})


        return attrs

    def create(self, validated_data):
        try:
            documentType = validated_data.pop('documentType')
        except KeyError:
            documentType = None

        try:
            genderAtBirth = validated_data.pop('genderAtBirth')
        except KeyError:
            genderAtBirth = None

        try:
            genderOfChoice = validated_data.pop('genderOfChoice')
        except KeyError:
            genderOfChoice = None

        try:
            location = validated_data.pop('location')
        except KeyError:
            location = None

        try:
            civilStatus = validated_data.pop('civilStatus')
        except KeyError:
            civilStatus = None

        #location = Location.objects.filter(pk=location['id'])

        profesional = Profesional.objects.create(
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
            notes=validated_data.get('notes'),
            primaryPhoneNumber=validated_data.get('primaryPhoneNumber'),
            primaryPhoneContact=validated_data.get('primaryPhoneContact'),
            primaryPhoneMessage=validated_data.get('primaryPhoneMessage'),
            documentType=documentType,
            genderAtBirth=genderAtBirth,
            genderOfChoice=genderOfChoice,
            location=location,
            civilStatus=civilStatus,
        )

        prestaciones = validated_data.pop('prestaciones')
        if prestaciones:
            for prestacion in prestaciones:
                db_prestaciones = Prestacion.objects.filter(pk=prestacion.get('id'))
                if db_prestaciones:
                    profesional.prestaciones.add(db_prestaciones[0])

        profesional.save()

        return profesional

    def update(self, instance, validated_data):
        documentType = validated_data.pop('documentType')
        genderAtBirth = validated_data.pop('genderAtBirth')
        genderOfChoice = validated_data.pop('genderOfChoice')
        location = validated_data.pop('location')
        location = Location.objects.filter(pk=location['id'])
        civilStatus = validated_data.pop('civilStatus')
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
        instance.notes = validated_data.get('notes', instance.notes)
        instance.primaryPhoneNumber = validated_data.get('primaryPhoneNumber', instance.primaryPhoneNumber)
        instance.primaryPhoneContact = validated_data.get('primaryPhoneContact', instance.primaryPhoneContact)
        instance.primaryPhoneMessage = validated_data.get('primaryPhoneMessage', instance.primaryPhoneMessage)
        instance.documentType = documentType
        instance.genderAtBirth = genderAtBirth
        instance.genderOfChoice = genderOfChoice
        instance.location = location[0]
        instance.civilStatus = civilStatus

        instance.prestaciones.clear()
        prestaciones = validated_data.pop('prestaciones')
        #print prestaciones
        if prestaciones:
            for prestacion in prestaciones:
                #print prestacion
                db_prestaciones = Prestacion.objects.filter(pk=prestacion.get('id'))
                if db_prestaciones:
                    instance.prestaciones.add(db_prestaciones[0])

        instance.save()

        return instance

    class Meta:
        model = Profesional
        extra_kwargs = {
            "id": {
                "read_only": False,
                "required": False,
            },
        }
        fields = ('id', 'firstName', 'otherNames', 'fatherSurname', 'motherSurname', 'birthDate', 'email',
                  'street', 'postal', 'status', 'documentType', 'documentNumber', 'genderAtBirth',
                  'genderOfChoice', 'location', 'occupation', 'civilStatus', 'notes', 'primaryPhoneNumber',
                  'primaryPhoneContact', 'primaryPhoneMessage', 'prestaciones')
