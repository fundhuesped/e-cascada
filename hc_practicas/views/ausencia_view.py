#!/usr/bin/python
# -*- coding: utf-8 -*-

from rest_framework import generics
from rest_framework.permissions import AllowAny
from rest_framework.pagination import PageNumberPagination
from hc_practicas.serializers import AusenciaNestSerializer
from hc_practicas.models import Ausencia
from datetime import datetime


class AusenciaList(generics.ListCreateAPIView):
    serializer_class = AusenciaNestSerializer
    queryset = Ausencia.objects.all()
    #permission_classes = (AllowAny,)

    def get_queryset(self):
        queryset = Ausencia.objects.all()
        day = self.request.query_params.get('day')
        if day is not None:
            queryset = queryset.filter(day=day)
        day__gte = self.request.query_params.get('day__gte')
        if day__gte is not None:
            queryset = queryset.filter(day__gte=day__gte)
        profesional = self.request.query_params.get('profesional')
        if profesional is not None:
            queryset = queryset.filter(profesional=profesional)

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


class AusenciaDetails(generics.RetrieveDestroyAPIView): #No se permite modificar una ausencia
    serializer_class = AusenciaNestSerializer
    queryset = Ausencia.objects.all()
    #permission_classes = (AllowAny,)
