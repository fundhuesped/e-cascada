#!/usr/bin/python
# -*- coding: utf-8 -*-

from rest_framework import serializers
from hc_practicas.models import Profesional

class ProfesionalNestedSerializer(serializers.ModelSerializer):
    """
    Serializa un profesional, para ser incluida como objeto nested en otro objeto
    """
    id = serializers.IntegerField()
    firstName = serializers.ReadOnlyField()
    otherNames = serializers.ReadOnlyField()
    fatherSurname = serializers.ReadOnlyField()
    motherSurname = serializers.ReadOnlyField()
    birthDate = serializers.ReadOnlyField()

    url = serializers.HyperlinkedIdentityField(
        view_name='hc_practicas:Profesional-detail',
        lookup_field='pk'
    )

    def to_internal_value(self, data):
        personas= Profesional.objects.filter(pk=data['id'])
        if personas[0] is not None:
            return personas[0]
        else:
            raise ValueError('Profesional not found')


    class Meta:
        model = Profesional
        fields = ('id', 'firstName', 'otherNames', 'fatherSurname', 'motherSurname', 'birthDate', 'url')