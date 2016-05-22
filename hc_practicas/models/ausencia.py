#!/usr/bin/python
# -*- coding: utf-8 -*-

from django.db import models
from hc_common.models import ActiveModel
from hc_practicas.models import Profesional, Turno

"""
Representa la ausencia de un profesional en un dia determinado
"""
class Ausencia(ActiveModel):
    day = models.DateField(null=False)
    start = models.TimeField(default='00:00:00')
    end = models.TimeField(default='23:59:59')
    profesional = models.ForeignKey(Profesional, null=True)
    status = models.CharField(max_length=8, choices=ActiveModel.STATUS_CHOICES, default=ActiveModel.STATUS_ACTIVE)

    #Cuando se elimina una ausencia, habilita los turnos asociados a esa fecha
    def delete(self, using=None, keep_parents=False):
        turnos = Turno.objects.filter(day=self.day, profesional=self.profesional)
        for turno in turnos:
            if (turno.start >= self.start and turno.start <= self.end) or (turno.end <= self.end and turno.end >= self.start):
                turno.status=Turno.STATUS_ACTIVE
                turno.save()
        super(Ausencia, self).delete(using, keep_parents)
