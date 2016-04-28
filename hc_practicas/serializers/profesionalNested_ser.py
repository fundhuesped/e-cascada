#!/usr/bin/python
# -*- coding: utf-8 -*-

from rest_framework import serializers
from hc_practicas.models import Profesional

class ProfesionalNestedSerializer(serializers.ModelSerializer):
    """
    Serializa un profesional, para ser incluida como objeto nested en otro objeto
    """
    ##TODO: Terminarlo como nested
    id = serializers.IntegerField()
    name = serializers.ReadOnlyField()
    description = serializers.ReadOnlyField()
    status = serializers.ReadOnlyField()
    duration = serializers.ReadOnlyField()
    default = serializers.ReadOnlyField()
    notes = serializers.ReadOnlyField()

    url = serializers.HyperlinkedIdentityField(
        view_name='hc_practicas:Prestacion-detail',
        lookup_field='pk'
    )

    def to_internal_value(self, data):
        profesionales= Profesional.objects.filter(pk=data['id'])
        if profesionales[0] is not None:
            return profesionales[0]
        else:
            raise ValueError('Profesional not found')


    class Meta:
        model = Profesional
        fields = ('id', 'name', 'description', 'status', 'duration', 'default', 'notes', 'url')