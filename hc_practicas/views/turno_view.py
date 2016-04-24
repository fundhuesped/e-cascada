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
        taken = self.request.query_params.get('taken')
        
        if taken is not None:
            value = self.str2bool(taken)    
            queryset = queryset.filter(taken=value)
        #day_from = self.request.query_params.get('from')
        #if day_from is None:
        #    day_from = datetime.now()
        #day_to = self.request.query_params.get('to')
        #if day_to is None:
        #    day_to = datetime.now()
        #queryset = queryset.filter(day__range=(day_from, day_to))
        day = self.request.query_params.get('day')
        if day is not None:
            queryset = queryset.filter(day=day)

        prestacion = self.request.query_params.get('prestacion')
        if prestacion is not None:
            queryset = queryset.filter(prestacion=prestacion)
        profesional = self.request.query_params.get('profesional')
        if profesional is not None:
            queryset = queryset.filter(profesional=profesional)

        paciente = self.request.query_params.get('paciente')
        if paciente is not None:
            queryset = queryset.filter(paciente = paciente)

        #Order  
        order_field = self.request.query_params.get('order_field')
        order_by = self.request.query_params.get('order_by')
        if (order_field is not None) and (order_by is not None):
            if order_by is 'asc':
                queryset = queryset.order_by(order_field)
            else:
                if order_by is 'desc':
                    queryset = queryset.order_by('-'+order_field)


        return queryset

    def str2bool(self, v):
        return v.lower() in ("yes", "true", "t", "1")


class TurnoDetails(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = TurnoNestSerializer
    queryset = Turno.objects.all()
    permission_classes = (AllowAny,)
