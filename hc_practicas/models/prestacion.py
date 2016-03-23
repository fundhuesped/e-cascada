#!/usr/bin/python
# -*- coding: utf-8 -*-

from django.db import models
from hc_practicas.models import Especialidad

class Prestacion(models.Model):

    STATUS_ACTIVE = 'Active'
    STATUS_INACTIVE = 'Inactive'

    STATUS_CHOICES = (
        (STATUS_ACTIVE, 'Activo'),
        (STATUS_INACTIVE, 'Inactivo')
    )

    name = models.CharField(max_length=70, null=False)
    description = models.CharField(max_length=150, null=False)
    duration = models.IntegerField(default=0)
    status = models.CharField(max_length=8, choices=STATUS_CHOICES, default=STATUS_ACTIVE)
    notes = models.CharField(blank=True, max_length=150, null=True)
    default = models.NullBooleanField(default=False)
    especialidad = models.ForeignKey(Especialidad, on_delete=models.CASCADE, related_name='prestaciones')