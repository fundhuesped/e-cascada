#!/usr/bin/python
# -*- coding: utf-8 -*-

from rest_framework import generics
from rest_framework.permissions import AllowAny
from procedures.serializers import PerformedSerializer
from procedures.models import ProcedurePeriod, Performed

class PerformedList(generics.ListCreateAPIView):
    """
    Vista para listar Period existentes, o crear un nuevo Period
    """
    serializer_class = PerformedSerializer
    queryset = Performed.objects.all()
    permission_classes = (AllowAny,)
    paginate_by = 20

class PerformedDetails(generics.RetrieveUpdateDestroyAPIView):
    """
    Vista para ver del detalle, modificar, o eliminar un Period
    """
    serializer_class = PerformedSerializer
    queryset = Performed.objects.all()
    permission_classes = (AllowAny,)
