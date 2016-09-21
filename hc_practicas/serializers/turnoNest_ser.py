#!/usr/bin/python
# -*- coding: utf-8 -*-

import datetime as dt

from django.db import transaction
from django.utils.translation import gettext as _
from hc_pacientes.serializers import PacienteNestedSerializer
from hc_practicas.models import Turno
from hc_practicas.services import turnoSlot_service
from hc_practicas.services import turno_service
from hc_practicas.serializers import TurnoSlotNestedSerializer

from rest_framework import serializers


class TurnoNestSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.ReadOnlyField()

    paciente = PacienteNestedSerializer(
        many=False
    )

    turnoSlot = TurnoSlotNestedSerializer(
        many=False,
        required=False
    )

    @transaction.atomic
    def create(self, validated_data):
        turno_slot = validated_data.get('turnoSlot')
        paciente = validated_data.get('paciente')
        notes = validated_data.get('notes')

        if turno_slot.day < dt.date.today():
            raise serializers.ValidationError({'error': _('No se pueden tomar turnos ya pasados')})

        instance = turno_service.create_turno(turno_slot, paciente, notes)
        turnoSlot_service.occupy_turno_slot(turno_slot)

        return instance

    @transaction.atomic
    def update(self, instance, validated_data):
        state = validated_data.get('state')
        notes = validated_data.get('notes')

        if instance.state != state:
            if instance.state == Turno.STATE_INITIAL:
                if state == Turno.STATE_PRESENT:
                    instance.state = Turno.STATE_PRESENT
                elif state == Turno.STATE_ABSENT:
                    instance.state = Turno.STATE_ABSENT
                elif state == Turno.STATE_CANCELED:
                    turnoSlot_service.release_turno_slot(instance.turnoSlot)
                    instance.state = Turno.STATE_CANCELED
                else:
                    raise serializers.ValidationError({'error': _('Estado incorrecto')})
            elif instance.state == Turno.STATE_PRESENT:
                if state == Turno.STATE_SERVED:
                    instance.state = Turno.STATE_SERVED
                else:
                    raise serializers.ValidationError({'error': _('Estado incorrecto')})
            else:
                raise serializers.ValidationError({'error': _('Estado incorrecto')})

        instance.notes = notes
        instance.save()
        return instance

    class Meta:
        model = Turno
        fields = ('id', 'paciente', 'turnoSlot', 'state', 'status', 'notes')
