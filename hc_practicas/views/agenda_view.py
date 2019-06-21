#!/usr/bin/python
# -*- coding: utf-8 -*-

import rest_framework_filters as r_f_filters

from hc_core.views import PaginateListCreateAPIView
from hc_practicas.models import Agenda
from hc_practicas.serializers import AgendaListSerializer
from hc_practicas.serializers import AgendaNestSerializer
from rest_framework import filters
from rest_framework import generics
from django_filters.rest_framework import DjangoFilterBackend



class AgendaFilter(r_f_filters.FilterSet):
    """
    Configura los campos por los que se puede fitrar
    """
    class Meta(object):
        """
        Define por diccionario los que se puede fitrar
        """
        model = Agenda
        fields = {
            'validFrom': r_f_filters.ALL_LOOKUPS,
            'status': r_f_filters.ALL_LOOKUPS,
            'validTo': r_f_filters.ALL_LOOKUPS
        }

class AgendaList(PaginateListCreateAPIView):
    """
    Vista para listar los elementos y crear uno nuevo
    """
    serializer_class = AgendaNestSerializer
    queryset = Agenda.objects.all()
    filter_backends = (filters.OrderingFilter, DjangoFilterBackend)
    filter_class = AgendaFilter

    def list(self, request, *args, **kwargs):
        self.serializer_class = AgendaListSerializer
        return super(AgendaList, self).list(request, *args, **kwargs)

    def get_queryset(self):
        queryset = Agenda.objects.all()
        serializer = AgendaListSerializer(queryset, many=True)

        profesional = self.request.query_params.get('profesional')
        prestacion = self.request.query_params.get('prestacion')
        if profesional is not None:
            queryset = queryset.filter(profesional__id=profesional)
        if prestacion is not None:
            queryset = queryset.filter(prestacion__id=prestacion)
        
        validToGte = self.request.query_params.get('validToGte')
        if validToGte is not None:
            queryset = queryset.filter(validTo__gte=validToGte)

        validToLt = self.request.query_params.get('validToLt')
        if validToLt is not None:
            queryset = queryset.filter(validTo__lt=validToLt)

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
    """
    Vista para solicitar un recurso y modificarlo
    """
    serializer_class = AgendaNestSerializer
    queryset = Agenda.objects.all()
    #permission_classes = (AllowAny,)
    
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.disable(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)

    def disable(self, instance):
        instance.status = Agenda.STATUS_INACTIVE
        instance.save()