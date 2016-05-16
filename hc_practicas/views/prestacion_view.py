#!/usr/bin/python
# -*- coding: utf-8 -*-

from rest_framework import generics
from rest_framework.permissions import AllowAny
from hc_practicas.serializers import PrestacionNestSerializer
from hc_practicas.models import Prestacion, Profesional

class PrestacionList(generics.ListCreateAPIView):
    """
    Vista para listar Prestaciones existentes, o crear una nueva Prestacion
    """
    serializer_class = PrestacionNestSerializer
    queryset = Prestacion.objects.all()
    permission_classes = (AllowAny,)
    paginate_by = 20

    def get_queryset(self):
        """
        Filtrado opcional del query, en base a name (valida que comience con los datos dados)
        """
        queryset = Prestacion.objects.all()
        name = self.request.query_params.get('name')
        status = self.request.query_params.get('status')
        especialidad = self.request.query_params.get('especialidad')
        profesional = self.request.query_params.get('profesional')
        if name is not None:
            queryset = queryset.filter(name__startswith=name)
        if status is not None:
            queryset = queryset.filter(status=status)
        if especialidad is not None:
            queryset = queryset.filter(especialidad__id=especialidad)
        if profesional is not None:
            prof = Profesional.objects.get(pk=profesional)
            if prof is not None:
                prestaciones = prof.prestaciones.values_list('pk')
                queryset = queryset.filter(pk__in=prestaciones)

        return queryset

class PrestacionDetails(generics.RetrieveUpdateDestroyAPIView):
    """
    Vista para ver del detalle, modificar, o eliminar una Prestacion
    """
    serializer_class = PrestacionNestSerializer
    queryset = Prestacion.objects.all()
    permission_classes = (AllowAny,)