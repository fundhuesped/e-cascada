#!/usr/bin/python
# -*- coding: utf-8 -*-

from rest_framework import generics
from rest_framework.permissions import AllowAny
from hc_practicas.serializers import EspecialidadNestSerializer
from hc_practicas.models import Especialidad,Profesional
from hc_core.views.paginateListCreateAPIView import PaginateListCreateAPIView


class EspecialidadList(PaginateListCreateAPIView):
    """
    Vista para listar Especialidades existentes, o crear una nueva Especialidad
    """
    serializer_class = EspecialidadNestSerializer
    queryset = Especialidad.objects.all()

    def get_queryset(self):
        """
        Filtrado opcional del query, en base a name (valida que comience con los datos dados)
        """
        queryset = Especialidad.objects.all()
        name = self.request.query_params.get('name')
        status = self.request.query_params.get('status')
        profesional = self.request.query_params.get('profesional')

        if name is not None:
            queryset = queryset.filter(name__startswith=name)

        if status is not None:
            queryset = queryset.filter(status=status)
        if profesional is not None:
            prof = Profesional.objects.get(pk=profesional)
            if prof is not None:
                especialidades_id = prof.prestaciones.values_list('especialidad_id')
                queryset = queryset.filter(pk__in=especialidades_id)
        #Order  
        order_field = self.request.query_params.get('order_field')
        order_by = self.request.query_params.get('order_by')
        if (order_field is not None) and (order_by is not None):
            if order_by == 'asc':
                queryset = queryset.order_by(order_field)
            else:
                if order_by == 'desc':
                    queryset = queryset.order_by('-'+order_field)


        return queryset

class EspecialidadDetails(generics.RetrieveUpdateDestroyAPIView):
    """
    Vista para ver del detalle, modificar, o eliminar una Especialidad
    """
    serializer_class = EspecialidadNestSerializer
    queryset = Especialidad.objects.all()
    #permission_classes = (AllowAny,)
