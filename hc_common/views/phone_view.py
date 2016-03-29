#!/usr/bin/python
# -*- coding: utf-8 -*-

from rest_framework import generics
from rest_framework.permissions import AllowAny
from hc_common.serializers import PhoneNestSerializer
from hc_common.models import Phone


class PhoneList(generics.ListCreateAPIView):
    """
    Vista para listar Documentos existentes, o crear un nuevo Documento
    """
    serializer_class = PhoneNestSerializer
    queryset = Phone.objects.all()
    permission_classes = (AllowAny,)
    paginate_by = 5


class PhoneDetails(generics.RetrieveUpdateDestroyAPIView):
    """
    Vista para ver del detalle, modificar, o eliminar un Documento
    """
    serializer_class = PhoneNestSerializer
    queryset = Phone.objects.all()
    permission_classes = (AllowAny,)
