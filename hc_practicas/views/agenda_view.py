#!/usr/bin/python
# -*- coding: utf-8 -*-

from rest_framework import generics
from rest_framework.permissions import AllowAny
from hc_practicas.serializers import AgendaNestSerializer
from hc_practicas.models import Agenda


class AgendaList(generics.ListCreateAPIView):
    serializer_class = AgendaNestSerializer
    queryset = Agenda.objects.all()
    #permission_classes = (AllowAny,)


    def get_queryset(self):
        queryset = Agenda.objects.all()
        status = self.request.query_params.get('status')
        profesional = self.request.query_params.get('profesional')
        prestacion = self.request.query_params.get('prestacion')

        if status is not None:
            queryset = queryset.filter(status=status)
        if profesional is not None:
            queryset = queryset.filter(profesional__id=profesional)
        if prestacion is not None:
            queryset = queryset.filter(prestacion__id=prestacion)

        return queryset


class AgendaDetails(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = AgendaNestSerializer
    queryset = Agenda.objects.all()
    #permission_classes = (AllowAny,)
