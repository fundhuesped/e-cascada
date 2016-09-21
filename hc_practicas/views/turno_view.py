#!/usr/bin/python
# -*- coding: utf-8 -*-

import rest_framework_filters as r_f_filters

from rest_framework import generics, filters
from rest_framework.permissions import AllowAny
from hc_practicas.serializers import TurnoNestSerializer
from hc_practicas.models import Turno
from hc_core.views import PaginateListCreateAPIView

class TurnoFilter(r_f_filters.FilterSet):
    """
    Configura los campos por los que se puede fitrar
    """
    class Meta(object):
        """
        Define por diccionario los que se puede fitrar
        """
        model = Turno
        fields = {
            'status': r_f_filters.ALL_LOOKUPS,
            'state': r_f_filters.ALL_LOOKUPS
        }

class TurnoList(PaginateListCreateAPIView):
    """
    Vista para listar los elementos y crear uno nuevo
    """
    serializer_class = TurnoNestSerializer
    queryset = Turno.objects.all()
    filter_backends = (filters.OrderingFilter,)
    ordering_fields = ('turnoSlot__day')
    ordering = ('-turnoSlot__day')
    
    def get_queryset(self):
        queryset = Turno.objects.all()

        paciente = self.request.query_params.get('paciente')
        if paciente is not None:
            queryset = queryset.filter(paciente=paciente)

        status = self.request.query_params.get('status')
        if status is not None:
            queryset = queryset.filter(status=status)

        state = self.request.query_params.get('state')
        if state is not None:
            queryset = queryset.filter(state=state)

        turno_slot = self.request.query_params.get('turnoSlot')
        if turno_slot is not None:
            queryset = queryset.filter(turnoSlot=turno_slot)

        return queryset

class TurnoDetails(generics.RetrieveUpdateDestroyAPIView):
    """
    Vista para solicitar un recurso y modificarlo
    """
    serializer_class = TurnoNestSerializer
    queryset = Turno.objects.all()
    permission_classes = (AllowAny,)
