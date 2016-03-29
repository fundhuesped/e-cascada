#!/usr/bin/python
# -*- coding: utf-8 -*-

from django.db import models
from hc_common.models import AbstractType, Location


class Address(AbstractType):
    location = models.ForeignKey(Location, on_delete=models.CASCADE, related_name='addressLocation', null=False)
