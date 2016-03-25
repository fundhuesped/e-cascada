#!/usr/bin/python
# -*- coding: utf-8 -*-

from rest_framework import serializers
from hc_common.models import Persona, DocumentType, SexType

class PersonaSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.ReadOnlyField()

    documentType = serializers.HyperlinkedRelatedField(
        view_name="hc_common:DocumentType-detail",
        queryset=DocumentType.objects
    )

    genderAtBirth = serializers.HyperlinkedRelatedField(
        view_name="hc_common:SexType-detail",
        queryset=SexType.objects
    )

    genderOfChoice = serializers.HyperlinkedRelatedField(
        view_name="hc_common:SexType-detail",
        queryset=SexType.objects
    )

    def create(self, validated_data):
        return Persona.objects.create(**validated_data)

    class Meta:
        model = Persona
        fields = ('id', 'firstName', 'otherNames', 'fatherSurname', 'motherSurname', 'birthDate', 'documentNumber', 'documentType', 'genderAtBirth', 'genderOfChoice', 'email', 'telephone')
