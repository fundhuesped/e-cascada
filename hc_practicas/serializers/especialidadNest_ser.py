#!/usr/bin/python
# -*- coding: utf-8 -*-

from rest_framework import serializers
from hc_practicas.models import Prestacion, Especialidad
from hc_practicas.serializers import PrestacionNestedSerializer

class EspecialidadNestSerializer(serializers.ModelSerializer):
    """
    Serializa una Especialidad
    """
    id = serializers.ReadOnlyField()

    prestaciones = PrestacionNestedSerializer(
        many=True,
        read_only=True
    )

    def create(self, validated_data):
        especialidad = Especialidad.objects.create(
            name = validated_data.get('name'),
            description = validated_data.get('description'),
            default = validated_data.get('default', False),
            status = validated_data.get('status'),
        )

        return especialidad

    def update(self, instance, validated_data):
        instance.name= validated_data.get('name', instance.name)
        instance.description = validated_data.get('description', instance.description)
        instance.default = validated_data.get('default', instance.default)
        instance.status = validated_data.get('status', instance.status)
        instance.save()
        
        #Cascadeo de cambio de estado
        prestaciones = Prestacion.objects.filter(especialidad=instance)
        for prestacion in prestaciones:
            #TODO HUES-259:Check if the prestacion was disabled due to disabling the especialidad or its disabled anyway
            prestacion.status=instance.status
            prestacion.save()

        return instance


    class Meta:
        model = Especialidad
        fields = ('id', 'name', 'default', 'description', 'status', 'prestaciones')