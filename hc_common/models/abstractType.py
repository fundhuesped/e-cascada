#!/usr/bin/python
# -*- coding: utf-8 -*-

from django.db import models


class AbstractType(models.Model):
    STATUS_ACTIVE = 'Active'
    STATUS_INACTIVE = 'Inactive'

    STATUS_CHOICES = (
        (STATUS_ACTIVE, 'Activo'),
        (STATUS_INACTIVE, 'Inactivo')
    )

    name = models.CharField(max_length=70, null=False)
    description = models.CharField(max_length=150, null=True)
    status = models.CharField(max_length=8, choices=STATUS_CHOICES, default=STATUS_ACTIVE)

    class Meta:
        abstract = True
