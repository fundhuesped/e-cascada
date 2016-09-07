#!/usr/bin/python
# -*- coding: utf-8 -*-

from django.db import models
from hc_practicas.models import Period

class DayOfWeek(models.Model):
    """
    Modelo un dia de la semana de un periodo de una agenda
    """
    index = models.IntegerField(null=False, default=0)
    name = models.CharField(max_length=20, null=False)
    period = models.ForeignKey(Period, related_name='daysOfWeek')
    selected = models.BooleanField()
