#!/usr/bin/python
# -*- coding: utf-8 -*-

from rest_framework import generics
from rest_framework.permissions import AllowAny
from hc_common.serializers import SexTypeNestSerializer
from hc_common.models import SexType


class SexTypeList(generics.ListCreateAPIView):
    """
    Vista para listar Documentos existentes, o crear un nuevo Documento
    """
    serializer_class = SexTypeNestSerializer
    queryset = SexType.objects.all()
    #permission_classes = (AllowAny,)
    paginate_by = 20

    def get_queryset(self):
        queryset = SexType.objects.all()
        name = self.request.query_params.get('name')
        status = self.request.query_params.get('status')
        if name is not None:
            queryset = queryset.filter(name__startswith=name)
        if status is not None:
            queryset = queryset.filter(status=status)
        return queryset


class SexTypeDetails(generics.RetrieveUpdateDestroyAPIView):
    """
    Vista para ver del detalle, modificar, o eliminar un Documento
    """
    serializer_class = SexTypeNestSerializer
    queryset = SexType.objects.all()
    #permission_classes = (AllowAny,)
