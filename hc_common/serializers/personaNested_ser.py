#!/usr/bin/python
# -*- coding: utf-8 -*-

from rest_framework import serializers
from hc_common.models import Persona

class PersonaNestedSerializer(serializers.ModelSerializer):
    """
    Serializa una persona, para ser incluida como objeto nested en otro objeto
    """
    id = serializers.IntegerField()
    firstName = serializers.ReadOnlyField()
    otherNames = serializers.ReadOnlyField()
    fatherSurname = serializers.ReadOnlyField()
    motherSurname = serializers.ReadOnlyField()
    birthDate = serializers.ReadOnlyField()

    url = serializers.HyperlinkedIdentityField(
        view_name='hc_common:Persona-detail',
        lookup_field='pk'
    )

    def to_internal_value(self, data):
        personas= Persona.objects.filter(pk=data['id'])
        if personas[0] is not None:
            return personas[0]
        else:
            raise ValueError('Especialidad not found')


    class Meta:
        model = Persona
        fields = ('id', 'firstName', 'otherNames', 'fatherSurname', 'motherSurname', 'birthDate', 'url')