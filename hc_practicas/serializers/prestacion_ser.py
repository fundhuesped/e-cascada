#!/usr/bin/python
# -*- coding: utf-8 -*-

from rest_framework import serializers
from hc_practicas.models import Prestacion, Especialidad

class PrestacionSerializer(serializers.HyperlinkedModelSerializer):
    """
    Serializa una Prestacion
    """
    id = serializers.ReadOnlyField()
    especialidad = serializers.HyperlinkedRelatedField(
        view_name="hc_practicas:Especialidad-detail",
        queryset=Especialidad.objects
    )
    def create(self, validated_data):
        """
        Crea una Prestacion
        :param validated_data: Valores con los cuales crear la Prestacion
        :return: Una nueva instancia de Prestacion
        """
        return Prestacion.objects.create(**validated_data)


    class Meta:
        model = Prestacion
        fields = ('id', 'name', 'description', 'status', 'duration', 'default', 'notes', 'especialidad')