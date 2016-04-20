#!/usr/bin/python
# -*- coding: utf-8 -*-

from django.db import models
from hc_practicas.models import DayOfWeek


class Period(models.Model):
    start = models.TimeField()
    end = models.TimeField()
    selected = models.BooleanField()
    daysOfWeek = models.ManyToManyField(DayOfWeek)
