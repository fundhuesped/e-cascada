#!/usr/bin/python
# -*- coding: utf-8 -*-

from django.utils import timezone
from django.db import models
from hc_common.models import ActiveModel
from hc_practicas.models import Profesional, Turno

"""
Representa la ausencia de un profesional en un dia determinado
"""
class Ausencia(ActiveModel):
    start_day = models.DateField(null=False, default=timezone.now)
    end_day = models.DateField(null=False, default=timezone.now)
    profesional = models.ForeignKey(Profesional, null=True)
    status = models.CharField(max_length=8, choices=ActiveModel.STATUS_CHOICES, default=ActiveModel.STATUS_ACTIVE)
    reason = models.CharField(blank=True, max_length=150, null=False)
    notes = models.CharField(blank=True, max_length=150, null=True)

    #Cuando se elimina una ausencia, habilita los turnos asociados a esa fecha
    def delete(self, using=None, keep_parents=False):
        turnos = Turno.objects.filter(day__range=[self.start_day,self.end_day], profesional=self.profesional)
        for turno in turnos:
            turno.status=Turno.STATUS_ACTIVE
            turno.save()
        super(Ausencia, self).delete(using, keep_parents)
