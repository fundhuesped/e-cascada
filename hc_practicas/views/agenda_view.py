#!/usr/bin/python
# -*- coding: utf-8 -*-

from rest_framework import generics
from rest_framework.permissions import AllowAny
from hc_practicas.serializers import AgendaNestSerializer
from hc_practicas.models import Agenda


class AgendaList(generics.ListCreateAPIView):
    serializer_class = AgendaNestSerializer
    queryset = Agenda.objects.all()
    permission_classes = (AllowAny,)
    paginate_by = 20

    def get_queryset(self):
        queryset = Agenda.objects.all()
        status = self.request.query_params.get('status')
        if status is not None:
            queryset = queryset.filter(status=status)
        return queryset


class AgendaDetails(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = AgendaNestSerializer
    queryset = Agenda.objects.all()
    permission_classes = (AllowAny,)
