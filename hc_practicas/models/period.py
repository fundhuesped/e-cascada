#!/usr/bin/python
# -*- coding: utf-8 -*-

from django.db import models
from hc_practicas.models import Agenda

class Period(models.Model):
    """
    Modelo para un bloque de tiempo de una agenda
    """
    start = models.TimeField()
    end = models.TimeField()
    selected = models.BooleanField()
    agenda = models.ForeignKey(Agenda, related_name='periods')
