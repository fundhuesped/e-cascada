#!/usr/bin/python
# -*- coding: utf-8 -*-

from rest_framework import serializers
from hc_common.models import Persona

class PersonaSerializer(serializers.HyperlinkedModelSerializer):
    """
    Serializa una Persona
    """
    id = serializers.ReadOnlyField()
    documento = serializers.HyperlinkedRelatedField( #elemento read only, para relacionarlo con el documento
        read_only=True,
        view_name='hc_common:Documento-detail')

    def create(self, validated_data):
        """
        Crea una Persona
        :param validated_data: Valores con los cuales crear la Persona
        :return: Una nueva instancia de Persona
        """
        persona =  Persona.objects.create(**validated_data)
        return persona


    class Meta:
        model = Persona
        fields = ('id', 'firstName', 'otherNames', 'fatherSurname', 'motherSurname', 'documento', 'birthDate')