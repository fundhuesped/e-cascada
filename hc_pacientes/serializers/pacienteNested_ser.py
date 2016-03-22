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

    url = serializers.HyperlinkedIdentityField(
        view_name='hc_pacientes:Paciente-detail',
        lookup_field='pk'
    )

    def to_internal_value(self, data):
        personas= Paciente.objects.filter(pk=data['id'])
        if personas[0] is not None:
            return personas[0]
        else:
            raise ValueError('Paciente not found')


    class Meta:
        model = Paciente
        fields = ('id', 'firstName', 'otherNames', 'fatherSurname', 'motherSurname', 'birthDate', 'idpaciente', 'url')