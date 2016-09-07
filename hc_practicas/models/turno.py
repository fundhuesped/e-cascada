#!/usr/bin/python
# -*- coding: utf-8 -*-

from django.db import models
from hc_common.models import ActiveModel
from hc_practicas.models import Profesional, Prestacion, Agenda
from hc_pacientes.models import Paciente
import reversion

@reversion.register()
class Turno(ActiveModel):
    day = models.DateField(null=False)
    start = models.TimeField(default='08:00:00')
    end = models.TimeField(default='17:00:00')
    taken = models.BooleanField(default=False)
    status = models.CharField(max_length=8, choices=ActiveModel.STATUS_CHOICES,
                              default=ActiveModel.STATUS_ACTIVE)
    paciente = models.ForeignKey(Paciente, null=True)
    agenda = models.ForeignKey(Agenda, null=True)
    profesional = models.ForeignKey(Profesional, null=True)
    prestacion = models.ForeignKey(Prestacion, null=True)
    updated_on = models.DateField(auto_now=True)
