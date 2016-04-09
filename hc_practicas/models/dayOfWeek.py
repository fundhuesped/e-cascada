#!/usr/bin/python
# -*- coding: utf-8 -*-

from django.db import models


class DayOfWeek(models.Model):
    name = models.CharField(max_length=20, null=False)
    selected = models.BooleanField()
