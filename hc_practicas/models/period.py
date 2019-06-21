#!/usr/bin/python
# -*- coding: utf-8 -*-

import reversion
from django.db import models
from hc_practicas.models import Agenda

@reversion.register()
class Period(models.Model):
    """
    Modelo para un bloque de tiempo de una agenda
    """
    start = models.TimeField()
    end = models.TimeField()
    selected = models.BooleanField()
    agenda = models.ForeignKey(Agenda, related_name='periods', on_delete=models.DO_NOTHING)
