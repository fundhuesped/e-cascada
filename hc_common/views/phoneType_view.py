#!/usr/bin/python
# -*- coding: utf-8 -*-

from rest_framework import generics
from rest_framework.permissions import AllowAny
from hc_common.serializers import PhoneTypeSerializer
from hc_common.models import PhoneType


class PhoneTypeList(generics.ListCreateAPIView):
    """
    Vista para listar Documentos existentes, o crear un nuevo Documento
    """
    serializer_class = PhoneTypeSerializer
    queryset = PhoneType.objects.all()
    permission_classes = (AllowAny,)
    paginate_by = 5


class PhoneTypeDetails(generics.RetrieveUpdateDestroyAPIView):
    """
    Vista para ver del detalle, modificar, o eliminar un Documento
    """
    serializer_class = PhoneTypeSerializer
    queryset = PhoneType.objects.all()
    permission_classes = (AllowAny,)
