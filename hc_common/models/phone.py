#!/usr/bin/python
# -*- coding: utf-8 -*-

from django.db import models
from hc_common.models import PhoneType


class Phone(models.Model):
    type = models.ForeignKey(PhoneType)
    number = models.CharField(max_length=20, null=True)
    contact = models.CharField(max_length=70, null=True)
    message = models.BooleanField(null=False, default=False)
