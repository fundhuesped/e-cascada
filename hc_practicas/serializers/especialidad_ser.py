#!/usr/bin/python
# -*- coding: utf-8 -*-

from rest_framework import serializers
from hc_practicas.models import Especialidad, Prestacion

class EspecialidadSerializer(serializers.HyperlinkedModelSerializer):
    """
    Serializa una Especialidad
    """
    id = serializers.ReadOnlyField()

    prestaciones = serializers.HyperlinkedRelatedField( #colección read only, con las prestaciones asociadas a una especialidad
        read_only=True,
        many=True,
        view_name='hc_practicas:Especialidad-detail')

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
        fields = ('id', 'name', 'description', 'status', 'prestaciones')