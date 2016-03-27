#!/usr/bin/python
# -*- coding: utf-8 -*-

from rest_framework import generics
from rest_framework.permissions import AllowAny
from hc_common.serializers import SexTypeSerializer
from hc_common.models import SexType

class SexTypeList(generics.ListCreateAPIView):
    """
    Vista para listar Documentos existentes, o crear un nuevo Documento
    """
    serializer_class = SexTypeSerializer
    queryset = SexType.objects.all()
    permission_classes = (AllowAny,)
    paginate_by = 5


class SexTypeDetails(generics.RetrieveUpdateDestroyAPIView):
    """
    Vista para ver del detalle, modificar, o eliminar un Documento
    """
    serializer_class = SexTypeSerializer
    queryset = SexType.objects.all()
    permission_classes = (AllowAny,)