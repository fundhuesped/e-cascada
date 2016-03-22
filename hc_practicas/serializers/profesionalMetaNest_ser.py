#!/usr/bin/python
# -*- coding: utf-8 -*-

from rest_framework import serializers
from hc_practicas.models import Profesional, ProfesionalMeta
from hc_practicas.serializers import ProfesionalNestedSerializer

class ProfesionalMetaNestSerializer(serializers.ModelSerializer):
    """
    Serializa un Meta Profesional
    """
    id = serializers.ReadOnlyField()

    profesional = ProfesionalNestedSerializer(
        many=False
    )

    def create(self, validated_data):
        profesional = validated_data.pop('profesional')
        meta = ProfesionalMeta.objects.create(
            metaType = validated_data.get('metaType'),
            metaValue = validated_data.get('metaValue'),
            profesional = profesional
        )

        return meta

    def update(self, instance, validated_data):
        profesional = validated_data.pop('profesional')
        instance.metaType= validated_data.get('metaType', instance.metaType)
        instance.metaValue = validated_data.get('metaValue', instance.metaValue)
        instance.profesional = profesional
        instance.save()

        return instance


    class Meta:
        model = ProfesionalMeta
        fields = ('id', 'metaType', 'metaValue', 'profesional')