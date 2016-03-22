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
            status = validated_data.get('status'),
        )

        return especialidad

    def update(self, instance, validated_data):
        instance.name= validated_data.get('name', instance.name)
        instance.description = validated_data.get('description', instance.description)
        instance.status = validated_data.get('status', instance.status)
        instance.save()

        return instance


    class Meta:
        model = Especialidad
        fields = ('id', 'name', 'description', 'status', 'prestaciones')