#!/usr/bin/python
# -*- coding: utf-8 -*-

from django.db import models
from procedures.models import ProcedurePeriod

class Performed(models.Model):
    performedDateTime = models.DateTimeField(null=True)
    performedPeriod = models.ForeignKey(ProcedurePeriod)
