#!/usr/bin/python
# -*- coding: utf-8 -*-

from django.db import models
from hc_common.models import ActiveModel
from hc_practicas.models import TurnoSlot
from hc_pacientes.models import Paciente
import reversion

@reversion.register()
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

    #El turno fue cancelado
    STATE_CANCELED = 'Canceled'

    #El turno fue cancelado e informado al paciente
    STATE_CANCELED_INFORMED = 'Canceled and informed'

    STATE_CHOICES = (
        (STATE_INITIAL, 'Inicial'),
        (STATE_PRESENT, 'Presente'),
        (STATE_ABSENT, 'Ausente'),
        (STATE_SERVED, 'Atendido'),
        (STATE_CANCELED, 'Cancelado'),
        (STATE_CANCELED_INFORMED, 'Cancelado e informado')
    )
    #Cancelacion por ausencia del profesional
    CANCELATION_PROFESIONAL_ABSENT = 'ProfesionalAbsent'

    #Cancelacion por cambio o baja de agenda
    CANCELATION_AGENDA_CHANGE = 'AgendaChanged'

    #Cancelacion a pedido del paciente
    CANCELATION_PACIENT_REQUEST = 'PacientRequest'

    #Cancelacion por otro motivo
    CANCELATION_OTHER = 'Other'

    CANCELATION_CHOICES = (
        (CANCELATION_PROFESIONAL_ABSENT, 'Ausencia del profesional'),
        (CANCELATION_AGENDA_CHANGE, 'Cambio o baja de agenda'),
        (CANCELATION_PACIENT_REQUEST, 'Pedido del paciente'),
        (CANCELATION_OTHER, 'Otro')
    )



    status = models.CharField(max_length=8,
                              choices=ActiveModel.STATUS_CHOICES,
                              default=ActiveModel.STATUS_ACTIVE)
    state = models.CharField(max_length=10,
                             choices=STATE_CHOICES,
                             null=False,
                             default=STATE_INITIAL)
    cancelation_reason = models.CharField(max_length=20, choices=CANCELATION_CHOICES, null=True)
    paciente = models.ForeignKey(Paciente, null=False)
    turnoSlot = models.ForeignKey(TurnoSlot, null=False, related_name='turnos')
    notes = models.CharField(blank=True, max_length=150, null=True)
    updated_on = models.DateField(auto_now=True)
    informed = models.BooleanField(default=False)
