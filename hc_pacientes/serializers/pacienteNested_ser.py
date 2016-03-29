#!/usr/bin/python
# -*- coding: utf-8 -*-

from rest_framework import serializers
from hc_pacientes.models import Paciente


class PacienteNestedSerializer(serializers.ModelSerializer):
    """
    Serializa un paciente, para ser incluida como objeto nested en otro objeto
    """
    id = serializers.IntegerField()
    firstName = serializers.ReadOnlyField()
    otherNames = serializers.ReadOnlyField()
    fatherSurname = serializers.ReadOnlyField()
    motherSurname = serializers.ReadOnlyField()
    birthDate = serializers.ReadOnlyField()
    idpaciente = serializers.ReadOnlyField()
    documentNumber = serializers.ReadOnlyField()
    email = serializers.ReadOnlyField()
    telephone = serializers.ReadOnlyField()
    status = serializers.ReadOnlyField()

    documentType = serializers.HyperlinkedIdentityField(
        view_name='hc_common:DocumentType-detail',
        lookup_field='pk'
    )
    genderAtBirth = serializers.HyperlinkedIdentityField(
        view_name='hc_common:SexType-detail',
        lookup_field='pk'
    )
    genderOfChoice = serializers.HyperlinkedIdentityField(
        view_name='hc_common:SexType-detail',
        lookup_field='pk'
    )
    telephones = serializers.HyperlinkedIdentityField(
        view_name='hc_common:Phone-detail',
        lookup_field='pk'
    )
    address = serializers.HyperlinkedIdentityField(
        view_name='hc_common:Address-detail',
        lookup_field='pk'
    )
    civilStatus = serializers.HyperlinkedIdentityField(
        view_name='hc_common:CivilStatusType-detail',
        lookup_field='pk'
    )
    socialService = serializers.HyperlinkedIdentityField(
        view_name='hc_common:SocialService-detail',
        lookup_field='pk'
    )
    education = serializers.HyperlinkedIdentityField(
        view_name='hc_common:EducationType-detail',
        lookup_field='pk'
    )
    url = serializers.HyperlinkedIdentityField(
        view_name='hc_common:Paciente-detail',
        lookup_field='pk'
    )

    def to_internal_value(self, data):
        personas = Paciente.objects.filter(pk=data['id'])
        if personas[0] is not None:
            return personas[0]
        else:
            raise ValueError('Paciente not found')

    class Meta:
        model = Paciente
        fields = ('id', 'firstName', 'otherNames', 'fatherSurname', 'motherSurname', 'birthDate', 'email', 'occupation',
                  'telephones', 'meta', 'address', 'civilStatus', 'socialService', 'socialNumber', 'education', 'terms',
                  'status', 'documentType', 'documentNumber', 'genderAtBirth', 'genderOfChoice', 'url')
