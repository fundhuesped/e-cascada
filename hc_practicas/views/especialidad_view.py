#!/usr/bin/python
# -*- coding: utf-8 -*-

from rest_framework import generics
from rest_framework.permissions import AllowAny
from hc_practicas.serializers import EspecialidadNestSerializer
from hc_practicas.models import Especialidad

class EspecialidadList(generics.ListCreateAPIView):
    """
    Vista para listar Especialidades existentes, o crear una nueva Especialidad
    """
    serializer_class = EspecialidadNestSerializer
    queryset = Especialidad.objects.all()
    permission_classes = (AllowAny,)
    paginate_by = 20

    def get_queryset(self):
        """
        Filtrado opcional del query, en base a name (valida que comience con los datos dados)
        """
        queryset = Especialidad.objects.all()
        name = self.request.query_params.get('name')
        status = self.request.query_params.get('status')
        if name is not None:
            queryset = queryset.filter(name__startswith=name)

        if status is not None:
            queryset = queryset.filter(status=status)

        return queryset

class EspecialidadDetails(generics.RetrieveUpdateDestroyAPIView):
    """
    Vista para ver del detalle, modificar, o eliminar una Especialidad
    """
    serializer_class = EspecialidadNestSerializer
    queryset = Especialidad.objects.all()
    permission_classes = (AllowAny,)