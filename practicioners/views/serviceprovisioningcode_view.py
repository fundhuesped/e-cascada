#!/usr/bin/python
# -*- coding: utf-8 -*-

from rest_framework import generics
from rest_framework.permissions import AllowAny
from practicioners.serializers import ServiceProvisioningCodeSerializer
from practicioners.models import ServiceProvisioningCode

class ServiceProvisioningCodeList(generics.ListCreateAPIView):
    """
    Vista para listar ServiceProvisioningCode existentes, o crear un nuevo ServiceProvisioningCode
    """
    serializer_class = ServiceProvisioningCodeSerializer
    queryset = ServiceProvisioningCode.objects.all()
    permission_classes = (AllowAny,)
    paginate_by = 20

class ServiceProvisioningCodeDetails(generics.RetrieveUpdateDestroyAPIView):
    """
    Vista para ver del detalle, modificar, o eliminar un ServiceProvisioningCode
    """
    serializer_class = ServiceProvisioningCodeSerializer
    queryset = ServiceProvisioningCode.objects.all()
    permission_classes = (AllowAny,)