#!/usr/bin/python
# -*- coding: utf-8 -*-

from rest_framework import generics
from rest_framework.permissions import AllowAny
from hc_practicas.serializers import PrestacionSerializer
from hc_practicas.models import Prestacion

class PrestacionList(generics.ListCreateAPIView):
    """
    Vista para listar Prestaciones existentes, o crear una nueva Prestacion
    """
    serializer_class = PrestacionSerializer
    queryset = Prestacion.objects.all()
    permission_classes = (AllowAny,)
    paginate_by = 20

    def get_queryset(self):
        """
        Filtrado opcional del query, en base a name (valida que comience con los datos dados)
        """
        queryset = Prestacion.objects.all()
        name = self.request.query_params.get('name')
        if name is not None:
            queryset = queryset.filter(name__startswith=name)

        return queryset

class PrestacionDetails(generics.RetrieveUpdateDestroyAPIView):
    """
    Vista para ver del detalle, modificar, o eliminar una Prestacion
    """
    serializer_class = PrestacionSerializer
    queryset = Prestacion.objects.all()
    permission_classes = (AllowAny,)