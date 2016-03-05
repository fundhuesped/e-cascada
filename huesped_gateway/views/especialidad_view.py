#!/usr/bin/python
# -*- coding: utf-8 -*-

from rest_framework import generics
from rest_framework.permissions import AllowAny
from huesped_gateway.serializers import EspecialidadSerializer
from huesped_gateway.models import Especialidad

class EspecialidadList(generics.ListCreateAPIView):
    """
    Vista para listar Especialidades existentes, o crear una nueva Especialidad
    """
    serializer_class = EspecialidadSerializer
    queryset = Especialidad.objects.all()
    permission_classes = (AllowAny,)
    paginate_by = 20

    def get_queryset(self):
        """
        Filtrado opcional del query, en base a name (valida que comience con los datos dados)
        """
        queryset = Especialidad.objects.all()
        name = self.request.query_params.get('name')

        if name is not None:
            queryset = queryset.filter(name__startswith=name)
        return queryset

class EspecialidadDetails(generics.RetrieveUpdateDestroyAPIView):
    """
    Vista para ver del detalle, modificar, o eliminar una Especialidad
    """
    serializer_class = EspecialidadSerializer
    queryset = Especialidad.objects.all()
    permission_classes = (AllowAny,)