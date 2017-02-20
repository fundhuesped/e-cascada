#!/usr/bin/python
# -*- coding: utf-8 -*-

from rest_framework import serializers
from hc_practicas.models import Period
from hc_practicas.serializers import DayOfWeekNestedSerializer


class PeriodNestSerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField()

    daysOfWeek = DayOfWeekNestedSerializer(
        many=True
    )

    def create(self, validated_data):
        daysOfWeek = validated_data.pop('daysOfWeek')
        custom = Period.objects.create(
            start=validated_data.get('start'),
            end=validated_data.get('end'),
            selected=validated_data.get('selected')
        )

        for dow in daysOfWeek:
            custom.daysOfWeek.add(dow)
        return custom

    def update(self, instance, validated_data):
        daysOfWeek = validated_data.pop('daysOfWeek')
        instance.start = validated_data.get('start', instance.start)
        instance.end = validated_data.get('end', instance.end)
        instance.selected = validated_data.get('selected', instance.selected)

        instance.daysOfWeek.clear()

        for dow in daysOfWeek:
            instance.daysOfWeek.add(dow)

        instance.save()

        return instance

    class Meta:
        model = Period
        fields = ('id', 'start', 'end', 'selected', 'daysOfWeek')
