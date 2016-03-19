#!/usr/bin/python
# -*- coding: utf-8 -*-

from rest_framework import serializers
from hc_practicas.models import Especialidad, Prestacion

class EspecialidadNestedSerializer(serializers.ModelSerializer):
    """
    Serializa una especialidad, para ser incluida como objeto nested en otro objeto
    """
    id = serializers.IntegerField()
    name = serializers.ReadOnlyField()
    #description = serializers.ReadOnlyField()
    #status = serializers.ReadOnlyField()

    url = serializers.HyperlinkedIdentityField(
        view_name='hc_practicas:Especialidad-detail',
        lookup_field='pk'
    )

    def to_internal_value(self, data):
        especialidades= Especialidad.objects.filter(pk=data['id'])
        if especialidades[0] is not None:
            return especialidades[0]
        else:
            raise ValueError('Especialidad not found')


    class Meta:
        model = Especialidad
        fields = ('id', 'name', 'url')

class EspecialidadSerializer(serializers.HyperlinkedModelSerializer):
    """
    Serializa una Especialidad
    """
    id = serializers.ReadOnlyField()

    prestaciones = serializers.HyperlinkedRelatedField( #colección read only, con las prestaciones asociadas a una especialidad
        read_only=True,
        many=True,
        view_name='hc_practicas:Prestacion-detail')

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