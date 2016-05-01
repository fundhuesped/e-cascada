#!/usr/bin/python
# -*- coding: utf-8 -*-

from django.db import models
from hc_common.models import ActiveModel
from hc_practicas.models import Period, Profesional, Prestacion


class Agenda(ActiveModel):
    start = models.TimeField()
    end = models.TimeField()
    validFrom = models.DateField(null=False, blank=True)
    validTo = models.DateField(null=False, blank=True)
    periods = models.ManyToManyField(Period)
    status = models.CharField(max_length=8, choices=ActiveModel.STATUS_CHOICES, default=ActiveModel.STATUS_ACTIVE)
    profesional = models.ForeignKey(Profesional, on_delete=models.CASCADE, related_name='profesional', null=True)
    prestacion = models.ForeignKey(Prestacion, on_delete=models.CASCADE, related_name='prestacion', null=True)
