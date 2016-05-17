#!/usr/bin/python
# -*- coding: utf-8 -*-

from rest_framework import generics
from rest_framework.permissions import AllowAny
from hc_practicas.serializers import ProfesionalNestSerializer
from hc_practicas.models import Profesional


class ProfesionalList(generics.ListCreateAPIView):
    """
    Vista para listar Profesionales existentes, o crear un nuevo Paciente
    """
    serializer_class = ProfesionalNestSerializer
    queryset = Profesional.objects.all()
    permission_classes = (AllowAny,)
    paginate_by = 20

    def get_queryset(self):
        """
        Filtrado del queryset por nombre y primer apellido, si como mínimo tienen 3 caracteres, o el ID de prestación
        :return:
        """
        queryset = Profesional.objects.all()
        firstName = self.request.query_params.get('firstName')
        fatherSurename = self.request.query_params.get('fatherSurename')
        prestacion = self.request.query_params.get('prestacion')
        especialidad = self.request.query_params.get('especialidad')

        if firstName is not None and len(firstName) > 3:
            queryset = queryset.filter(firstName__startswith=firstName)
        if fatherSurename is not None and len(fatherSurename) > 3:
            queryset = queryset.filter(fatherSurename__startswith=fatherSurename)
        if prestacion is not None:
            queryset = queryset.filter(prestaciones__pk__in=prestacion)
        if especialidad is not None:
            queryset = queryset.filter(prestaciones__especialidad__id=especialidad).distinct()

        return queryset


class ProfesionalDetails(generics.RetrieveUpdateDestroyAPIView):
    """
    Vista para ver del detalle, modificar, o eliminar un Profesional
    """
    serializer_class = ProfesionalNestSerializer
    queryset = Profesional.objects.all()
    permission_classes = (AllowAny,)
