#!/usr/bin/python
# -*- coding: utf-8 -*-

import reversion

from rest_framework import serializers
from hc_practicas.models import Ausencia
from hc_practicas.models import TurnoSlot
from hc_practicas.serializers import ProfesionalNestedSerializer
from hc_practicas.services import turnoSlot_service


class AusenciaNestSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.ReadOnlyField()

    profesional = ProfesionalNestedSerializer(
        many=False
    )

    def create(self, validated_data):
        profesional = validated_data.pop('profesional')
        instance = Ausencia.objects.create(
            start_day=validated_data.get('start_day'),
            end_day=validated_data.get('end_day'),
            profesional=profesional,
            notes=validated_data.get('notes'),
            reason=validated_data.get('reason')
        )

        # Cuando se crea una ausencia,
        # pasa a conflicto todos los turnosSlots del profesional asociado
        turno_slots = TurnoSlot.objects.filter(day__range=[instance.start_day, instance.end_day],
                                               profesional=instance.profesional,
                                               state__in=[TurnoSlot.STATE_AVAILABLE,
                                                          TurnoSlot.STATE_OCCUPIED])
        for turno_slot in turno_slots:
            turnoSlot_service.conflict_turno_slot_unaware(turno_slot)
        # Agrego datos de la revision
        reversion.set_user(self._context['request'].user)
        reversion.set_comment("Create Ausencia")
        return instance

    #Método agregado por compatibilidad. Las ausencias solo se pueden agregar o eliminar
    def update(self, instance, validated_data):
        profesional = validated_data.pop('profesional')
        instance.day = validated_data.get('day', instance.day)
        instance.start = validated_data.get('start', instance.start)
        instance.end = validated_data.get('end', instance.end)
        instance.profesional = profesional
        instance.save()
        # Agrego datos de la revision
        reversion.set_user(self._context['request'].user)
        reversion.set_comment("Updated Ausencia")
        return instance



    class Meta:
        model = Ausencia
        fields = ('id', 'start_day', 'end_day', 'profesional', 'status', 'reason', 'notes')
