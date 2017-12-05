#!/usr/bin/python
# -*- coding: utf-8 -*-

import datetime as dt

import reversion
from django.db import transaction
from django.utils.translation import gettext as _
from hc_pacientes.serializers import PacienteNestedSerializer
from hc_practicas.models import Turno
from hc_practicas.models import TurnoSlot
from hc_practicas.models import Profesional
from hc_practicas.models import Prestacion
from hc_practicas.services import turnoSlot_service
from hc_practicas.services import turno_service
from hc_practicas.serializers import TurnoSlotNestedSerializer
from datetime import datetime
from hc_core.serializers import UserNestedSerializer

from rest_framework import serializers


class SobreturnoNestSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.ReadOnlyField()

    paciente = PacienteNestedSerializer(
        many=False
    )

    turnoSlot = TurnoSlotNestedSerializer(
        many=False
    )

    lastModifiedBy = UserNestedSerializer(
        many=False,
        required=False,
        allow_null=True
    )

    createdBy = UserNestedSerializer(
        many=False,
        required=False,
        allow_null=True
    )

    @transaction.atomic
    def create(self, validated_data):
        # Agrego datos de la revision
        reversion.set_user(self._context['request'].user)
        reversion.set_comment("Created Sobreturno")

        turno_slot = validated_data.get('turnoSlot')

        paciente = validated_data.get('paciente')
        notes = validated_data.get('notes')
        prestacion = Prestacion.objects.get(pk=turno_slot['prestacion'])
        profesional = Profesional.objects.get(pk=turno_slot['profesional'])


        day = datetime.strptime(turno_slot['day'], '%Y-%m-%d')
        start = datetime.strptime(turno_slot['start'], '%H:%M')
        end = datetime.strptime(turno_slot['end'], '%H:%M')

        turno_slot_instance = TurnoSlot.objects.create(
            day=day,
            start=start,
            end=end,
            state=TurnoSlot.STATE_OCCUPIED,
            profesional=profesional,
            prestacion=prestacion
        )
        turno_slot_instance.save()

        instance = turno_service.create_turno(turno_slot_instance, paciente, self._context['request'].user, notes)

        return instance
    class Meta:
        model = Turno
        fields = ('id', 'paciente', 'turnoSlot', 'state', 'status', 'notes', 'lastModifiedBy', 'createdBy')        