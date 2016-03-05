#!/usr/bin/python
# -*- coding: utf-8 -*-

from django.db import models

#Clase Period
#Period handled by the Service Site
class ProcedurePeriod(models.Model):
    start = models.TimeField()                                         #Start time of day
    end = models.TimeField()                                           #End time of day
