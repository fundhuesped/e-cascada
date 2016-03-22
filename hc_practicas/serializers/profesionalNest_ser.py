#!/usr/bin/python
# -*- coding: utf-8 -*-

from rest_framework import serializers
from hc_practicas.models import Profesional, ProfesionalMeta
from hc_practicas.serializers import ProfesionalMetaNestedSerializer, PrestacionNestedSerializer

class ProfesionalNestSerializer(serializers.ModelSerializer):
    """
    Serializa un Profesional
    """
    id = serializers.ReadOnlyField()

    meta = ProfesionalMetaNestedSerializer(
        many=True,
        read_only=True
    )

    prestaciones = PrestacionNestedSerializer(
        many=True,
        read_only=False
    )

    def create(self, validated_data):
        prestaciones = validated_data.pop('prestaciones')
        profesional = Profesional.objects.create(**validated_data)
        for prestacion in prestaciones:
            profesional.prestaciones.add(prestacion)
        profesional.save()

        return profesional

    def update(self, instance, validated_data):
        prestaciones = validated_data.pop('prestaciones')

        instance.firstName= validated_data.get('firstName', instance.firstName)
        instance.otherNames = validated_data.get('otherNames', instance.otherNames)
        instance.fatherSurname = validated_data.get('fatherSurname', instance.fatherSurname)
        instance.motherSurname = validated_data.get('motherSurname', instance.motherSurname)
        instance.birthDate = validated_data.get('birthDate', instance.birthDate)


        instance.prestaciones.clear()

        for prestacion in prestaciones:
            instance.prestaciones.add(prestacion)

        instance.save()

        return instance


    class Meta:
        model = Profesional
        fields = ('id', 'firstName', 'otherNames', 'fatherSurname', 'motherSurname', 'birthDate', 'prestaciones', 'meta')