#!/usr/bin/python
# -*- coding: utf-8 -*-

from django.db import models
from hc_common.models import ActiveModel
from hc_practicas.models import TurnoSlot
from hc_pacientes.models import Paciente

class Turno(ActiveModel):
    """
    Clase que representa un turno otorgado a un paciente
    """

    #Estado inicial del turno
    STATE_INITIAL = 'Initial'

    #El paciente se encuentra presente en la insitution para asistir al turno
    STATE_PRESENT = 'Present'

    #El paciente no vino al turno
    STATE_ABSENT = 'Absent'

    #El paciente ya fue atendido
    STATE_SERVED = 'Served'

    #El turno fue cancelado el turno
    STATE_CANCELED = 'Canceled'

    STATE_CHOICES = (
        (STATE_INITIAL, 'Inicial'),
        (STATE_PRESENT, 'Presente'),
        (STATE_ABSENT, 'Ausente'),
        (STATE_SERVED, 'Atendido'),
        (STATE_CANCELED, 'Cancelado')
    )

    status = models.CharField(max_length=8, choices=ActiveModel.STATUS_CHOICES,
                              default=ActiveModel.STATUS_ACTIVE)
    state = models.CharField(max_length=10, choices=STATE_CHOICES, null=False, default=STATE_INITIAL)
    paciente = models.ForeignKey(Paciente, null=False)
    turnoSlot = models.ForeignKey(TurnoSlot, null=False, related_name='turnos')
    notes = models.CharField(blank=True, max_length=150, null=True)
    updated_on = models.DateField(auto_now=True)
