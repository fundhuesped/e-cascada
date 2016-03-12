#!/usr/bin/python
# -*- coding: utf-8 -*-

from rest_framework import serializers
from hc_common.models import Documento, Persona

class DocumentoSerializer(serializers.HyperlinkedModelSerializer):
    """
    Serializa un Documento
    """
    id = serializers.ReadOnlyField()
    persona = serializers.HyperlinkedRelatedField(
        view_name="hc_common:Persona-detail",
        queryset=Persona.objects
    )

    def create(self, validated_data):
        """
        Crea un Documento
        :param validated_data: Valores con los cuales crear el Documento
        :return: Una nueva instancia de Documento
        """
        especialidad =  Documento.objects.create(**validated_data)
        return especialidad


    class Meta:
        model = Documento
        fields = ('id', 'type', 'number', 'comments', 'persona')