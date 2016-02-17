#!/usr/bin/python
# -*- coding: utf-8 -*-

from rest_framework import generics
from rest_framework.permissions import AllowAny
from practicioners.serializers import SpecialitySerializer
from practicioners.models import Speciality

class SpecialityList(generics.ListCreateAPIView):
    """
    Vista para listar Speciality existentes, o crear un nuevo Speciality
    """
    serializer_class = SpecialitySerializer
    queryset = Speciality.objects.all()
    permission_classes = (AllowAny,)
    paginate_by = 20

class SpecialityDetails(generics.RetrieveUpdateDestroyAPIView):
    """
    Vista para ver del detalle, modificar, o eliminar un Speciality
    """
    serializer_class = SpecialitySerializer
    queryset = Speciality.objects.all()
    permission_classes = (AllowAny,)