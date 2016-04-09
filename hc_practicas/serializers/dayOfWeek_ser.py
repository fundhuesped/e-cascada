#!/usr/bin/python
# -*- coding: utf-8 -*-

from rest_framework import serializers
from hc_practicas.models import DayOfWeek


class DayOfWeekSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.ReadOnlyField()

    def create(self, validated_data):
        custom = DayOfWeek.objects.create(**validated_data)
        return custom

    class Meta:
        model = DayOfWeek
        fields = ('id', 'name', 'selected')
