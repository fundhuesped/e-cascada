#!/usr/bin/python
# -*- coding: utf-8 -*-

from rest_framework import generics
from rest_framework.permissions import AllowAny
from rest_framework.pagination import PageNumberPagination
from hc_practicas.serializers import TurnoNestSerializer
from hc_practicas.models import Turno
from datetime import datetime


class TurnoList(generics.ListCreateAPIView):
    serializer_class = TurnoNestSerializer
    queryset = Turno.objects.all()
    #permission_classes = (AllowAny,)



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
    #permission_classes = (AllowAny,)
