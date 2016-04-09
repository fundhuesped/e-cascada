#!/usr/bin/python
# -*- coding: utf-8 -*-

from rest_framework import serializers
from hc_practicas.models import DayOfWeek


class DayOfWeekNestSerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField()

    def create(self, validated_data):
        custom = DayOfWeek.objects.create(
            name=validated_data.get('name'),
            selected=validated_data.get('selected')
        )

        return custom

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.selected = validated_data.get('selected', instance.selected)
        instance.save()

        return instance

    class Meta:
        model = DayOfWeek
        fields = ('id', 'name', 'selected')
