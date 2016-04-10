#!/usr/bin/python
# -*- coding: utf-8 -*-

from django.db import models
from hc_common.models import ActiveModel
from hc_practicas.models import Profesional, Prestacion
from hc_pacientes.models import Paciente


class Turno(ActiveModel):
    day = models.DateField(null=False)
    start = models.TimeField()
    end = models.TimeField()
    taken = models.BooleanField(default=False)
    paciente = models.ForeignKey(Paciente, null=True)
    profesional = models.ForeignKey(Profesional, null=True)
    prestacion = models.ForeignKey(Prestacion, null=True)
