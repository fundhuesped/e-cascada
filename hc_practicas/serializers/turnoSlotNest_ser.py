#!/usr/bin/python
# -*- coding: utf-8 -*-

from hc_practicas.models import TurnoSlot
from hc_practicas.serializers import PrestacionNestedSerializer
from hc_practicas.serializers import ProfesionalNestedSerializer
from hc_practicas.serializers import TurnoNestedSerializer
from rest_framework import serializers


class TurnoSlotNestSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.ReadOnlyField()

    profesional = ProfesionalNestedSerializer(
        many=False
    )

    prestacion = PrestacionNestedSerializer(
        many=False
    )

    turnos = TurnoNestedSerializer(
        many=True
    )

    class Meta:
        model = TurnoSlot
        fields = ('id', 'day', 'start', 'end', 'profesional', 'prestacion', 'status', 'state', 'turnos')
