#!/usr/bin/python
# -*- coding: utf-8 -*-

from django.db import models
from hc_common.models import ActiveModel
from hc_practicas.models import Profesional, Prestacion, Agenda


class TurnoSlot(ActiveModel):
    """
    Clase que representa un slot de tiempo que puede ser tomado por un turno
    """

    STATE_AVAILABLE = 'Available'
    STATE_OCCUPIED = 'Occupied'
    STATE_CONFLICT = 'Conflict'
    STATE_DELETED = 'Deleted'

    STATE_CHOICES = (
        (STATE_AVAILABLE, 'Disponible'),
        (STATE_OCCUPIED, 'Ocupado'),
        (STATE_CONFLICT, 'En conflicto'),
        (STATE_DELETED, 'Eliminado')
    )

    day = models.DateField(null=False)
    start = models.TimeField(default='08:00:00')
    end = models.TimeField(default='17:00:00')
    status = models.CharField(max_length=8, choices=ActiveModel.STATUS_CHOICES,
                              default=ActiveModel.STATUS_ACTIVE)
    state = models.CharField(max_length=10, choices=STATE_CHOICES, null=False)
    agenda = models.ForeignKey(Agenda, null=True)
    profesional = models.ForeignKey(Profesional, null=True)
    prestacion = models.ForeignKey(Prestacion, null=True)
    updated_on = models.DateField(auto_now=True)
