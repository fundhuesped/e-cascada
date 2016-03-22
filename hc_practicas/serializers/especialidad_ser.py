#!/usr/bin/python
# -*- coding: utf-8 -*-

from rest_framework import serializers
from hc_practicas.models import Especialidad

class EspecialidadSerializer(serializers.HyperlinkedModelSerializer):
    """
    Serializa una Especialidad
    """
    id = serializers.ReadOnlyField()

    def create(self, validated_data):
        """
        Crea una Especialidad
        :param validated_data: Valores con los cuales crear la Especialidad
        :return: Una nueva instancia de Especialidad
        """
        especialidad =  Especialidad.objects.create(**validated_data)
        return especialidad


    class Meta:
        model = Especialidad
        fields = ('id', 'name', 'description', 'status')