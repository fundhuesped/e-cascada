#!/usr/bin/python
# -*- coding: utf-8 -*-

from django.db import models
from hc_common.models import ActiveModel
from hc_practicas.models import Profesional, Prestacion
from hc_pacientes.models import Paciente


class Turno(ActiveModel):
    day = models.DateField(null=False)
    start = models.TimeField(default='08:00:00')
    end = models.TimeField(default='17:00:00')
    taken = models.BooleanField(default=False)
    paciente = models.ForeignKey(Paciente, null=True)
    profesional = models.ForeignKey(Profesional, null=True)
    prestacion = models.ForeignKey(Prestacion, null=True)
