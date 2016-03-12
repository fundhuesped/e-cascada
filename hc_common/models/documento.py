#!/usr/bin/python
# -*- coding: utf-8 -*-

from django.db import models
from hc_common.models import Persona

class Documento(models.Model):
    """
    Clase que representa la información mínima necesaria para gestionar un Documento
    """
    TYPE_DNI = 'DNI'
    TYPE_PASSPORT = 'PASS'
    TYPE_OTHER = 'OTHER'

    TYPE_CHOICES = (
        (TYPE_DNI, 'Documento Nacional de Identidad'),
        (TYPE_PASSPORT, 'Pasaporte'),
        (TYPE_OTHER, 'Otro')
    )

    type = models.CharField(max_length=5, choices=TYPE_CHOICES, default=TYPE_DNI, null=False)
    number = models.BigIntegerField(null=False)
    comments = models.CharField(max_length=200, null=True)
    persona = models.OneToOneField(Persona, related_name='documento', on_delete=models.CASCADE, null=True)