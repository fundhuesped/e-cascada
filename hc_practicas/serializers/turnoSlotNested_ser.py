#!/usr/bin/python
# -*- coding: utf-8 -*-

from rest_framework import serializers
from hc_practicas.models import TurnoSlot
from hc_practicas.serializers import ProfesionalNestedSerializer
from hc_practicas.serializers import PrestacionNestedSerializer

class TurnoSlotNestedSerializer(serializers.ModelSerializer):
    """
    Serializa un TurnoSlot, para ser incluida como objeto nested en otro objeto
    """
    id = serializers.IntegerField()
    day = serializers.ReadOnlyField()
    start = serializers.ReadOnlyField()
    end = serializers.ReadOnlyField()
    state = serializers.ReadOnlyField()
    status = serializers.ReadOnlyField()

    profesional = ProfesionalNestedSerializer(
        many=False,
        read_only=True
    )

    prestacion = PrestacionNestedSerializer(
        many=False,
        read_only=True
    )

    def to_internal_value(self, data):
        if (isinstance(data, list) or isinstance(data, dict)):
            turno_slots= TurnoSlot.objects.filter(pk=data['id'])
        else:
            turno_slots=TurnoSlot.objects.filter(pk=data)
        if turno_slots.count() > 0:
            return turno_slots[0]
        else:
            raise ValueError('TurnoSlot not found')


    class Meta:
        model = TurnoSlot
        fields = ('id', 'day', 'start', 'end', 'status', 'state', 'profesional', 'prestacion' )