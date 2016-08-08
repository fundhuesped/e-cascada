#!/usr/bin/python
# -*- coding: utf-8 -*-

from rest_framework import generics, filters
from rest_framework.permissions import AllowAny
from hc_practicas.serializers import TurnoNestSerializer
from hc_practicas.models import Turno
from hc_core.views import PaginateListCreateAPIView


class TurnoList(PaginateListCreateAPIView):
    serializer_class = TurnoNestSerializer
    queryset = Turno.objects.all()
    filter_backends = (filters.OrderingFilter,)

    def get_queryset(self):
        queryset = Turno.objects.all()
        taken = self.request.query_params.get('taken')

        if taken is not None:
            value = self.str2bool(taken)
            queryset = queryset.filter(taken=value)

        day = self.request.query_params.get('day')
        if day is not None:
            queryset = queryset.filter(day=day)

        day__gte = self.request.query_params.get('day__gte')
        if day__gte is not None:
            queryset = queryset.filter(day__gte=day__gte)

        prestacion = self.request.query_params.get('prestacion')
        if prestacion is not None:
            queryset = queryset.filter(prestacion=prestacion)

        profesional = self.request.query_params.get('profesional')
        if profesional is not None:
            queryset = queryset.filter(profesional=profesional)

        status = self.request.query_params.get('status')
        if status is not None:
            queryset = queryset.filter(status=status)

        paciente = self.request.query_params.get('paciente')
        if paciente is not None:
            queryset = queryset.filter(paciente=paciente)

        start = self.request.query_params.get('start')
        if start is not None:
            queryset = queryset.filter(day__gte=start)

        end = self.request.query_params.get('end')
        if end is not None:
            queryset = queryset.filter(day__lte=end)

        return queryset

    def str2bool(self, v):
        return v.lower() in ("yes", "true", "t", "1")


class TurnoDetails(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = TurnoNestSerializer
    queryset = Turno.objects.all()
    permission_classes = (AllowAny,)
