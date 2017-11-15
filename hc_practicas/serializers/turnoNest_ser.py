#!/usr/bin/python
# -*- coding: utf-8 -*-

import datetime as dt

import reversion
from django.db import transaction
from django.utils.translation import gettext as _
from hc_pacientes.serializers import PacienteNestedSerializer
from hc_practicas.models import Turno
from hc_practicas.models import TurnoSlot
from hc_practicas.services import turnoSlot_service
from hc_practicas.services import turno_service
from hc_practicas.serializers import TurnoSlotNestedSerializer
from hc_notificaciones.serializers import NotificationSMSSerializer
from hc_notificaciones.serializers import NotificationEmailSerializer
from hc_core.serializers import UserNestedSerializer


from rest_framework import serializers


class TurnoNestSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.ReadOnlyField()

    paciente = PacienteNestedSerializer(
        many=False
    )

    lastModifiedBy = UserNestedSerializer(
        many=False
    )

    createdBy = UserNestedSerializer(
        many=False
    )

    turnoSlot = TurnoSlotNestedSerializer(
        many=False,
        required=False
    )

    @transaction.atomic
    def create(self, validated_data):
        # Agrego datos de la revision
        reversion.set_user(self._context['request'].user)
        reversion.set_comment("Created Turno")

        turno_slot = validated_data.get('turnoSlot')
        paciente = validated_data.get('paciente')
        notes = validated_data.get('notes')


        if turno_slot.day < dt.date.today():
            raise serializers.ValidationError({'error': _('No se pueden tomar turnos ya pasados')})

        if turno_slot.state != TurnoSlot.STATE_AVAILABLE:
            raise serializers.ValidationError({'error': _('El turno ya se encuentra tomado')})

        instance = turno_service.create_turno(turno_slot, paciente, self._context['request'].user, notes)
        turnoSlot_service.occupy_turno_slot(turno_slot)

        return instance

    @transaction.atomic
    def update(self, instance, validated_data):
        # Agrego datos de la revision
        reversion.set_user(self._context['request'].user)
        reversion.set_comment("Modified Turno")

        state = validated_data.get('state')
        notes = validated_data.get('notes')
        informed = validated_data.get('informed')

        if instance.state != state:
            if instance.state == Turno.STATE_INITIAL:
                if state == Turno.STATE_PRESENT:
                    instance.state = Turno.STATE_PRESENT
                elif state == Turno.STATE_ABSENT:
                    instance.state = Turno.STATE_ABSENT
                elif state == Turno.STATE_CANCELED:
                    if instance.turnoSlot.agenda:
                        turnoSlot_service.release_turno_slot(instance.turnoSlot)
                    else:
                        turnoSlot_service.delete_turno_slot_unaware(instance.turnoSlot)
                    instance.state = Turno.STATE_CANCELED
                    instance.cancelation_reason = Turno.CANCELATION_PACIENT_REQUEST
                else:
                    raise serializers.ValidationError({'error': _('Estado incorrecto')})
            elif instance.state == Turno.STATE_PRESENT:
                if state == Turno.STATE_SERVED:
                    instance.state = Turno.STATE_SERVED
                else:
                    raise serializers.ValidationError({'error': _('Estado incorrecto')})
            elif instance.state == Turno.STATE_CANCELED:
                if state == Turno.STATE_CANCELED_INFORMED:
                    instance.state = Turno.STATE_CANCELED_INFORMED
                else:
                    raise serializers.ValidationError({'error': _('Estado incorrecto')})
            else:
                raise serializers.ValidationError({'error': _('Estado incorrecto')})

        instance.informed = informed
        instance.notes = notes
        instance.lastModifiedBy = self._context['request'].user;
        instance.save()
        return instance

    class Meta:
        model = Turno
        fields = ('id', 'paciente', 'turnoSlot', 'state', 'status', 'notes', 'cancelation_reason', 'createdBy', 'lastModifiedBy', 'informed')
