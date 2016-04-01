#!/usr/bin/python
# -*- coding: utf-8 -*-

from django.db import models
from hc_common.models import AbstractType, District


class Location(AbstractType):
    district = models.ForeignKey(District)
