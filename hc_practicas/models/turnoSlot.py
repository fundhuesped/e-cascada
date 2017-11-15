#!/usr/bin/python
# -*- coding: utf-8 -*-

from django.db import models
from django.db.models import Q
from hc_common.models import ActiveModel
from hc_practicas.models import Agenda
from hc_practicas.models import Prestacion
from hc_practicas.models import Profesional
from django.apps import apps
from django.core.exceptions import ObjectDoesNotExist
import reversion

@reversion.register()
class TurnoSlot(ActiveModel):
    """
    Clase que representa un slot de tiempo que puede ser tomado por un turno
    """
    def __str__(self):
        return "Sarasa"
    def __unicode__(self):
        return str(self.start)+'-'+str(self.end)+' '+str(self.day)

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

    @property
    def currentTurno(self):
        """
        Representaal turno que actualmente tiene ocupado este slot o devuelve vacio
        """
        turno_state = apps.get_model('hc_practicas','Turno').STATE_CANCELED
        try:
            currentTurno = self.turnos.get(~Q(state=turno_state))
            return currentTurno
        except ObjectDoesNotExist:
            return None
