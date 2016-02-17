#!/usr/bin/python
# -*- coding: utf-8 -*-

from django.db import models

#Periodo de tiempo en el que un PracticionerQualification es válido
#Period during which the qualification is valid
class PracticionerQualificationPeriod(models.Model):
    start = models.DateTimeField()
    end = models.DateTimeField()