#!/usr/bin/python
# -*- coding: utf-8 -*-

import reversion
from django.db import models
from hc_practicas.models import Period

@reversion.register()
class DayOfWeek(models.Model):
    """
    Modelo un dia de la semana de un periodo de una agenda
    """
    index = models.IntegerField(null=False, default=0)
    name = models.CharField(max_length=20, null=False)
    period = models.ForeignKey(Period, related_name='daysOfWeek', on_delete=models.DO_NOTHING)
    selected = models.BooleanField()
