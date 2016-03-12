#!/usr/bin/python
# -*- coding: utf-8 -*-

from django.db import models
from hc_common.models import Persona

class Paciente(Persona):
    """
    Clase que representa la información mínima necesaria para gestionar un Paciente
    """
    idpaciente = models.CharField(max_length=20, null=True)
