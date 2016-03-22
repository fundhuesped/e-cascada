#!/usr/bin/python
# -*- coding: utf-8 -*-

from rest_framework import generics
from rest_framework.permissions import AllowAny
from hc_common.serializers import DocumentoNestSerializer
from hc_common.models import Documento

class DocumentoList(generics.ListCreateAPIView):
    """
    Vista para listar Documentos existentes, o crear un nuevo Documento
    """
    serializer_class = DocumentoNestSerializer
    queryset = Documento.objects.all()
    permission_classes = (AllowAny,)
    paginate_by = 5


class DocumentoDetails(generics.RetrieveUpdateDestroyAPIView):
    """
    Vista para ver del detalle, modificar, o eliminar un Documento
    """
    serializer_class = DocumentoNestSerializer
    queryset = Documento.objects.all()
    permission_classes = (AllowAny,)