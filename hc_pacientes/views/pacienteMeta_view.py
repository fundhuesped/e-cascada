#!/usr/bin/python
# -*- coding: utf-8 -*-

from rest_framework import generics
from rest_framework.permissions import AllowAny
from hc_pacientes.serializers import PacienteMetaNestSerializer
from hc_pacientes.models import PacienteMeta

class PacienteMetaList(generics.ListCreateAPIView):
    """
    Vista para listar PacienteMetas existentes, o crear un nuevo PacienteMeta
    """
    serializer_class = PacienteMetaNestSerializer
    queryset = PacienteMeta.objects.all()
    permission_classes = (AllowAny,)
    paginate_by = 20

    def get_queryset(self):
        """
        Filtrado del queryset por nombre y primer apellido, si como mínimo tienen 3 caracteres
        :return:
        """
        queryset = PacienteMeta.objects.all()
        type = self.request.query_params.get('metaType')

        if (type is not None):
            queryset = queryset.filter(metaType=type)

        return queryset

class PacienteMetaDetails(generics.RetrieveUpdateDestroyAPIView):
    """
    Vista para ver del detalle, modificar, o eliminar un Documento
    """
    serializer_class = PacienteMetaNestSerializer
    queryset = PacienteMeta.objects.all()
    permission_classes = (AllowAny,)