#!/usr/bin/python
# -*- coding: utf-8 -*-

from rest_framework import serializers
from hc_practicas.models import Especialidad

class EspecialidadNestedSerializer(serializers.ModelSerializer):
    """
    Serializa una especialidad, para ser incluida como objeto nested en otro objeto
    """
    id = serializers.IntegerField()
    name = serializers.ReadOnlyField()
    description = serializers.ReadOnlyField()
    status = serializers.ReadOnlyField()

    url = serializers.HyperlinkedIdentityField(
        view_name='hc_practicas:Especialidad-detail',
        lookup_field='pk'
    )

    def to_internal_value(self, data):
        especialidades= Especialidad.objects.filter(pk=data['id'])
        if especialidades.count()>0:
            return especialidades[0]
        else:
            raise ValueError('Especialidad not found')


    class Meta:
        model = Especialidad
        fields = ('id', 'name', 'description', 'default', 'status', 'url')