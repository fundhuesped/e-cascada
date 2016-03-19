#!/usr/bin/python
# -*- coding: utf-8 -*-

from rest_framework import serializers
from hc_practicas.models import Prestacion, Especialidad
from hc_practicas.serializers import EspecialidadNestedSerializer

class PrestacionNestSerializer(serializers.ModelSerializer):
    """
    Serializa una Prestación
    """
    id = serializers.ReadOnlyField()

    especialidad = EspecialidadNestedSerializer(
        many=False
    )

    def create(self, validated_data):
        especialidad = validated_data.pop('especialidad')
        prestacion = Prestacion.objects.create(
            name = validated_data.get('name'),
            description = validated_data.get('description'),
            status = validated_data.get('status'),
            duration = validated_data.get('duration'),
            default = validated_data.get('default'),
            notes = validated_data.get('notes'),
            especialidad = especialidad
        )
        prestacion.save()

        return prestacion

    def update(self, instance, validated_data):
        especialidad = validated_data.pop('especialidad')
        instance.name= validated_data.get('name', instance.name)
        instance.description = validated_data.get('description', instance.description)
        instance.status = validated_data.get('status', instance.status)
        instance.duration = validated_data.get('duration', instance.duration)
        instance.default = validated_data.get('default', instance.duration)
        instance.notes = validated_data.get('notes', instance.notes)
        instance.especialidad = especialidad
        instance.save()

        return instance


    class Meta:
        model = Prestacion
        fields = ('id', 'name', 'description', 'status', 'duration', 'default', 'notes', 'especialidad')

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