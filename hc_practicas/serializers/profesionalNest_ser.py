#!/usr/bin/python
# -*- coding: utf-8 -*-

import reversion
import datetime as dt
import copy
from django.utils.translation import gettext as _
from hc_common.models import Location
from hc_common.serializers import DocumentTypeNestedSerializer
from hc_common.serializers import SexTypeNestedSerializer
from hc_practicas.models import Agenda
from hc_practicas.models import Prestacion
from hc_practicas.models import Profesional
from hc_practicas.serializers import PrestacionNestedSerializer
from rest_framework import serializers


class ProfesionalNestSerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField()
    status = serializers.CharField(
        default=Profesional.STATUS_ACTIVE
    )

    prestaciones = PrestacionNestedSerializer(
        many=True,
        read_only=False,
        allow_null=True,
        required=False
    )

    documentType = DocumentTypeNestedSerializer(
        many=False,
        required=False,
        allow_null=True
    )

    genderAtBirth = SexTypeNestedSerializer(
        many=False,
        required=False,
        allow_null=True
    )

    genderOfChoice = SexTypeNestedSerializer(
        many=False,
        required=False,
        allow_null=True
    )


    def validate(self, attrs):
        """
        Validaciones de datos básicos para el alta de un profesional
        :param attrs:
        :return:
        """

        #HUES-215: Solo son obligatorios nombre y apellido
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
        """

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


        profesional = Profesional.objects.create(
            firstName=validated_data.get('firstName'),
            otherNames=validated_data.get('otherNames'),
            fatherSurname=validated_data.get('fatherSurname'),
            motherSurname=validated_data.get('motherSurname'),
            municipalNumber=validated_data.get('municipalNumber'),
            licenseNumber=validated_data.get('licenseNumber'),
            birthDate=validated_data.get('birthDate'),
            documentNumber=validated_data.get('documentNumber'),
            email=validated_data.get('email'),
            status=validated_data.get('status'),
            notes=validated_data.get('notes'),
            primaryPhoneNumber=validated_data.get('primaryPhoneNumber'),
            primaryPhoneContact=validated_data.get('primaryPhoneContact'),
            primaryPhoneMessage=validated_data.get('primaryPhoneMessage'),
            title=validated_data.get('title'),
            documentType=documentType,
            genderAtBirth=genderAtBirth,
            genderOfChoice=genderOfChoice,
        )
        profesional.prestaciones.clear()
        prestaciones = validated_data.pop('prestaciones')
        if prestaciones:
            for prestacion in prestaciones:
                profesional.prestaciones.add(prestacion)

        profesional.save()
        # Agrego datos de la revision
        reversion.set_user(self._context['request'].user)
        reversion.set_comment("Created Profesional")

        return profesional

    def update(self, instance, validated_data):
        documentType = validated_data.pop('documentType')
        genderAtBirth = validated_data.pop('genderAtBirth')
        genderOfChoice = validated_data.pop('genderOfChoice')
        instance.firstName = validated_data.get('firstName', instance.firstName)
        instance.otherNames = validated_data.get('otherNames', instance.otherNames)
        instance.fatherSurname = validated_data.get('fatherSurname', instance.fatherSurname)
        instance.motherSurname = validated_data.get('motherSurname', instance.motherSurname)
        instance.municipalNumber = validated_data.get('municipalNumber', instance.municipalNumber)
        instance.licenseNumber = validated_data.get('licenseNumber', instance.licenseNumber)
        instance.birthDate = validated_data.get('birthDate', instance.birthDate)
        instance.documentNumber = validated_data.get('documentNumber', instance.documentNumber)
        instance.email = validated_data.get('email', instance.email)
        instance.notes = validated_data.get('notes', instance.notes)
        instance.title = validated_data.get('title')
        instance.primaryPhoneNumber = validated_data.get('primaryPhoneNumber', instance.primaryPhoneNumber)
        instance.primaryPhoneContact = validated_data.get('primaryPhoneContact', instance.primaryPhoneContact)
        instance.primaryPhoneMessage = validated_data.get('primaryPhoneMessage', instance.primaryPhoneMessage)
        instance.documentType = documentType
        instance.genderAtBirth = genderAtBirth
        instance.genderOfChoice = genderOfChoice
        status = validated_data.get('status', instance.status)

        # Agrego datos de la revision
        reversion.set_user(self._context['request'].user)
        reversion.set_comment("Modified Profesional")

        if instance.status != status:

            try:
                from hc_practicas.serializers import AgendaNestSerializer
            except ImportError:
                import sys
                AgendaNestSerializer = sys.modules[__package__ + '.AgendaNestSerializer']

            if instance.status == Profesional.STATUS_ACTIVE and status == Profesional.STATUS_INACTIVE:
                agenda_serializer = AgendaNestSerializer()
                instance.status = Profesional.STATUS_INACTIVE
                agendas = Agenda.objects.filter(profesional=instance,
                                                status=Agenda.STATUS_ACTIVE,
                                                validTo__gte=dt.date.today())
                for agenda in agendas:
                    agenda_serializer.deactivate(agenda)
                # Agrego datos de la revision
                reversion.set_comment("Deactivated Profesional")

            elif instance.status == Profesional.STATUS_INACTIVE and status == Profesional.STATUS_ACTIVE:
                instance.status = Profesional.STATUS_ACTIVE
                # Agrego datos de la revision
                reversion.set_comment("Activated Profesional")


        instance.prestaciones.clear()
        prestaciones = validated_data.pop('prestaciones')

        if prestaciones:
            for prestacion in prestaciones:
                instance.prestaciones.add(prestacion)

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
                  'status', 'documentType', 'documentNumber', 'genderAtBirth',
                  'genderOfChoice', 'notes', 'primaryPhoneNumber',
                  'primaryPhoneContact', 'primaryPhoneMessage', 'prestaciones', 'municipalNumber', 'licenseNumber', 'title')
