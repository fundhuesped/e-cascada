#!/usr/bin/python
# -*- coding: utf-8 -*-

from rest_framework import generics
from rest_framework.permissions import AllowAny
from hc_practicas.serializers import TurnoNestSerializer
from hc_practicas.models import Turno
from datetime import datetime


class TurnoList(generics.ListCreateAPIView):
    serializer_class = TurnoNestSerializer
    queryset = Turno.objects.all()
    permission_classes = (AllowAny,)
    paginate_by = 20

    def get_queryset(self):
        queryset = Turno.objects.all()
        status = self.request.query_params.get('status')
        if status is not None:
            queryset = queryset.filter(status=status)
        dayFrom = self.request.query_params.get('from')
        if dayFrom is None:
            dayFrom = datetime.now()
        dayTo = self.request.query_params.get('dayTo')
        if dayTo is None:
            dayTo = datetime.now()

        print dayFrom
        print dayTo
        queryset = queryset.filter(day__range=(dayFrom, dayTo))
        print queryset
        return queryset


class TurnoDetails(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = TurnoNestSerializer
    queryset = Turno.objects.all()
    permission_classes = (AllowAny,)
