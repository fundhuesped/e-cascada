#!/usr/bin/python
# -*- coding: utf-8 -*-

from rest_framework import serializers
from hc_practicas.models import Period
from hc_practicas.serializers import DayOfWeekNestSerializer


class PeriodNestSerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField()

    daysOfWeek = DayOfWeekNestSerializer(
        many=True
    )

    def create(self, validated_data):
        daysOfWeek = validated_data.pop('daysOfWeek')
        custom = Period.objects.create(
            start=validated_data.get('start'),
            end=validated_data.get('end'),
            selected=validated_data.get('selected'),
            daysOfWeek=daysOfWeek
        )

        return custom

    def update(self, instance, validated_data):
        daysOfWeek = validated_data.pop('daysOfWeek')
        instance.start = validated_data.get('start', instance.start)
        instance.end = validated_data.get('end', instance.end)
        instance.selected = validated_data.get('selected', instance.selected)
        instance.daysOfWeek = validated_data.get('daysOfWeek', instance.daysOfWeek)
        instance.save()

        return instance

    class Meta:
        model = Period
        fields = ('id', 'start', 'end', 'selected', 'daysOfWeek')
