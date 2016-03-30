#!/usr/bin/python
# -*- coding: utf-8 -*-

from rest_framework import serializers
from hc_practicas.models import Especialidad, Prestacion

class PrestacionNestedSerializer(serializers.ModelSerializer):
    """
    Serializa una especialidad, para ser incluida como objeto nested en otro objeto
    """
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
        prestaciones= Prestacion.objects.filter(pk=data['id'])
        if prestaciones[0] is not None:
            return prestaciones[0]
        else:
            raise ValueError('Prestacion not found')


    class Meta:
        model = Prestacion
        fields = ('id', 'name', 'description', 'status', 'duration', 'default', 'notes', 'url')