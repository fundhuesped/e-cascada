#!/usr/bin/python
# -*- coding: utf-8 -*-
from django.db import models
from hc_pacientes.models import Paciente

class PacienteMeta(models.Model):
    paciente = models.ForeignKey(Paciente, related_name='meta', null=True)
    metaType = models.CharField(max_length=10, null=False)
    metaValue = models.CharField(max_length=200, null=False)