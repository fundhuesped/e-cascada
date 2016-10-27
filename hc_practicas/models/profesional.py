#!/usr/bin/python
# -*- coding: utf-8 -*-

from django.db import models
from hc_common.models import Persona
from hc_practicas.models import Prestacion
import reversion

@reversion.register()
class Profesional(Persona):
    """
    Clase que representa la información mínima necesaria para gestionar un Profesional (quien ejerce una prestación)
    """
    prestaciones = models.ManyToManyField(Prestacion)
    municipalNumber = models.CharField(max_length=8, null=False)
    licenseNumber = models.CharField(max_length=8, null=False)
    updated_on = models.DateField(auto_now=True)
