#!/usr/bin/python
# -*- coding: utf-8 -*-

from django.db import models
from hc_practicas.models import Especialidad
from hc_common.models import ActiveModel


class Prestacion(ActiveModel):
    name = models.CharField(max_length=70, null=False)
    description = models.CharField(max_length=150, null=True, blank=True)
    duration = models.IntegerField(default=0)
    status = models.CharField(max_length=8, choices=ActiveModel.STATUS_CHOICES, default=ActiveModel.STATUS_ACTIVE)
    notes = models.CharField(blank=True, max_length=150, null=True)
    default = models.BooleanField(default=False)
    especialidad = models.ForeignKey(Especialidad, on_delete=models.CASCADE, related_name='prestaciones')

    class Meta:
        ordering = ['default','name']