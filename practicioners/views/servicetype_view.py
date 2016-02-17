#!/usr/bin/python
# -*- coding: utf-8 -*-

from practicioners.models import ServiceType
from practicioners.serializers import ServiceTypeSerializer
from rest_framework import generics
from rest_framework.permissions import AllowAny

class ServiceTypeList(generics.ListCreateAPIView):
    model = ServiceType
    serializer_class = ServiceTypeSerializer
    permission_classes = (AllowAny,)
    queryset = ServiceType.objects.all()

class ServiceTypeDetails(generics.RetrieveUpdateDestroyAPIView):
    """
    Devuelve, modifica o elimina una instancia de ServiceType
    """
    serializer_class = ServiceTypeSerializer
    queryset = ServiceType.objects.all()
    permission_classes = (AllowAny,)