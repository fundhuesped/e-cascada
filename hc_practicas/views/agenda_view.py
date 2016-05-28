#!/usr/bin/python
# -*- coding: utf-8 -*-

from rest_framework import generics
from rest_framework.permissions import AllowAny
from hc_practicas.serializers import AgendaNestSerializer
from hc_practicas.models import Agenda
from hc_core.views.paginateListCreateAPIView import PaginateListCreateAPIView


class AgendaList(PaginateListCreateAPIView):
    serializer_class = AgendaNestSerializer
    queryset = Agenda.objects.all()

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


class AgendaDetails(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = AgendaNestSerializer
    queryset = Agenda.objects.all()
    #permission_classes = (AllowAny,)
