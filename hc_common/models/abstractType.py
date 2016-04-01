#!/usr/bin/python
# -*- coding: utf-8 -*-

from django.db import models
from hc_common.models import ActiveModel


class AbstractType(ActiveModel):
    name = models.CharField(max_length=70, null=False)
    description = models.CharField(max_length=150, null=True)
    status = models.CharField(max_length=8, choices=ActiveModel.STATUS_CHOICES, default=ActiveModel.STATUS_ACTIVE)

    class Meta:
        abstract = True