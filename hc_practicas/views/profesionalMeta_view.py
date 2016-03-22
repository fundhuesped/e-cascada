#!/usr/bin/python
# -*- coding: utf-8 -*-

from rest_framework import generics
from rest_framework.permissions import AllowAny
from hc_practicas.serializers import ProfesionalMetaNestSerializer
from hc_practicas.models import ProfesionalMeta

class ProfesionalMetaList(generics.ListCreateAPIView):
    """
    Vista para listar Meta profesionales existentes, o crear un nuevo Meta profesional
    """
    serializer_class = ProfesionalMetaNestSerializer
    queryset = ProfesionalMeta.objects.all()
    permission_classes = (AllowAny,)
    paginate_by = 20

    def get_queryset(self):
        """
        Filtrado del queryset por metaType
        :return:
        """
        queryset = ProfesionalMeta.objects.all()
        type = self.request.query_params.get('metaType')

        if (type is not None):
            queryset = queryset.filter(metaType=type)

        return queryset

class ProfesionalMetaDetails(generics.RetrieveUpdateDestroyAPIView):
    """
    Vista para ver del detalle, modificar, o eliminar un MEta Profesional
    """
    serializer_class = ProfesionalMetaNestSerializer
    queryset = ProfesionalMeta.objects.all()
    permission_classes = (AllowAny,)