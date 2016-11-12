#!/usr/bin/python
# -*- coding: utf-8 -*-

from rest_framework import generics, filters
from rest_framework.permissions import DjangoModelPermissions
from hc_practicas.serializers import PrestacionNestSerializer
from hc_practicas.models import Prestacion, Profesional
from hc_core.views import PaginateListCreateAPIView

class PrestacionList(PaginateListCreateAPIView):
    """
    Vista para listar Prestaciones existentes, o crear una nueva Prestacion
    """
    serializer_class = PrestacionNestSerializer
    queryset = Prestacion.objects.all()
    filter_backends = (filters.OrderingFilter,)
    permission_classes = (DjangoModelPermissions,)

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
            queryset = queryset.filter(name__istartswith=name)
        if status is not None:
            queryset = queryset.filter(status=status)
        if especialidad is not None:
            queryset = queryset.filter(especialidad__id=especialidad)
        if profesional is not None:
            prof = Profesional.objects.get(pk=profesional)
            if prof is not None:
                prestaciones = prof.prestaciones.values_list('pk')
                queryset = queryset.filter(pk__in=prestaciones)
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

class PrestacionDetails(generics.RetrieveUpdateDestroyAPIView):
    """
    Vista para ver del detalle, modificar, o eliminar una Prestacion
    """
    serializer_class = PrestacionNestSerializer
    queryset = Prestacion.objects.all()
    permission_classes = (DjangoModelPermissions,)
