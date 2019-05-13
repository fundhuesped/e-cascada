#!/usr/bin/python
# -*- coding: utf-8 -*-

import rest_framework_filters as r_f_filters

from rest_framework import generics, filters
from rest_framework.permissions import DjangoModelPermissions
from hc_practicas.serializers import TurnoSlotNestSerializer
from hc_practicas.models import TurnoSlot
from hc_core.views import PaginateListAPIView
from django_filters import widgets

class TurnoSlotFilter(r_f_filters.FilterSet):
    """
    Configura los campos por los que se puede fitrar
    """

    # Filtro para multiples estados
    state = r_f_filters.MultipleChoiceFilter(choices=TurnoSlot.STATE_CHOICES,
                                             widget=widgets.CSVWidget())
    class Meta(object):
        """
        Define por diccionario los que se puede fitrar
        """
        model = TurnoSlot
        fields = ['state']
#        fields = {
#            'day': r_f_filters.ALL_LOOKUPS,
#            'prestacion': r_f_filters.ALL_LOOKUPS,
#            'profesional': r_f_filters.ALL_LOOKUPS,
#            'status': r_f_filters.ALL_LOOKUPS,
#            'start': r_f_filters.ALL_LOOKUPS,
#            'end': r_f_filters.ALL_LOOKUPS,
#            'state': r_f_filters.ALL_LOOKUPS
#        }

class TurnoSlotList(PaginateListAPIView):
    """
    Vista para listar los elementos y crear uno nuevo
    """
    serializer_class = TurnoSlotNestSerializer
    queryset = TurnoSlot.objects.all()
    filter_backends = (filters.OrderingFilter, filters.DjangoFilterBackend)
    filter_class = TurnoSlotFilter
    permission_classes = (DjangoModelPermissions,)

    def get_queryset(self):
        queryset = TurnoSlot.objects.all()

        day = self.request.query_params.get('day')
        if day is not None:
            queryset = queryset.filter(day=day)

        day__gte = self.request.query_params.get('day__gte')
        if day__gte is not None:
            queryset = queryset.filter(day__gte=day__gte)

        prestacion = self.request.query_params.get('prestacion')
        if prestacion is not None:
            queryset = queryset.filter(prestacion=prestacion)

        especialidad = self.request.query_params.get('especialidad')
        if especialidad is not None:
            queryset = queryset.filter(prestacion__espcialidad=especialidad)

        profesional = self.request.query_params.get('profesional')
        if profesional is not None:
            queryset = queryset.filter(profesional=profesional)

        status = self.request.query_params.get('status')
        if status is not None:
            queryset = queryset.filter(status=status)

        # state = self.request.query_params.get('state')
        # if state is not None:
        #     queryset = queryset.filter(state=state)

        start = self.request.query_params.get('start')
        if start is not None:
            queryset = queryset.filter(day__gte=start)

        end = self.request.query_params.get('end')
        if end is not None:
            queryset = queryset.filter(day__lte=end)

        return queryset

    def str2bool(self, v):
        return v.lower() in ("yes", "true", "t", "1")


class TurnoSlotDetails(generics.RetrieveAPIView):
    """
    Vista para solicitar un recurso y modificarlo
    """
    serializer_class = TurnoSlotNestSerializer
    queryset = TurnoSlot.objects.all()
    permission_classes = (DjangoModelPermissions,)
