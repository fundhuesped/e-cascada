#!/usr/bin/python
# -*- coding: utf-8 -*-

from rest_framework import serializers
from hc_common.models import SexType

class SexTypeSerializer(serializers.HyperlinkedModelSerializer):
    """
    Serializa un Tipo de Documento
    """
    id = serializers.ReadOnlyField()

    def create(self, validated_data):
        return SexType.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data['name']
        instance.description = validated_data['description']
        instance.save()
        return instance

    class Meta:
        model = SexType
        fields = ('id', 'name', 'description')