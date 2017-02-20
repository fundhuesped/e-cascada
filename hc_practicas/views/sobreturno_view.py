#!/usr/bin/python
# -*- coding: utf-8 -*-

from hc_practicas.models import Agenda
from hc_practicas.models import Ausencia
from hc_practicas.models import Turno
from hc_practicas.serializers import SobreturnoNestSerializer
from rest_framework import filters
from rest_framework import generics
from rest_framework.permissions import DjangoModelPermissions

from rest_framework.response import Response
from rest_framework import status

class SobreturnoCreate(generics.CreateAPIView):
    """
    Vista para crear sobreturnos
    """
    serializer_class = SobreturnoNestSerializer    
    permission_classes = (DjangoModelPermissions,)
    queryset = Turno.objects.none() 