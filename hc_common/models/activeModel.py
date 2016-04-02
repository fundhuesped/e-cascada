#!/usr/bin/python
# -*- coding: utf-8 -*-

from django.db import models


class ActiveModel(models.Model):
    STATUS_ACTIVE = 'Active'
    STATUS_INACTIVE = 'Inactive'

    STATUS_CHOICES = (
        (STATUS_ACTIVE, 'Activo'),
        (STATUS_INACTIVE, 'Inactivo')
    )

    class Meta:
        abstract = True
