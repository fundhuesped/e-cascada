#!/usr/bin/python
# -*- coding: utf-8 -*-

from django.db import models


class DayOfWeek(models.Model):
    index = models.IntegerField(null=False, default=0)
    name = models.CharField(max_length=20, null=False)
    selected = models.BooleanField()
