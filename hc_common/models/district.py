#!/usr/bin/python
# -*- coding: utf-8 -*-

from django.db import models
from hc_common.models import AbstractType, Province


class District(AbstractType):
    province = models.ForeignKey(Province)
