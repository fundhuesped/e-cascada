#!/usr/bin/python
# -*- coding: utf-8 -*-

from rest_framework import generics, filters
from rest_framework.permissions import AllowAny
from hc_practicas.serializers import TurnoNestSerializer
from hc_practicas.models import Turno, Ausencia, Agenda


class TurnoCancelado(generics.ListAPIView):
    serializer_class = TurnoNestSerializer
    queryset = Turno.objects.all()
    filter_backends = (filters.OrderingFilter,)
    permission_classes = (AllowAny,)

    def get_queryset(self):
        queryset = Turno.objects.all()

        start_day = None
        end_day = None
        profesionalId = None
        ausenciaId = self.request.query_params.get('ausencia')
        agendaId = self.request.query_params.get('agenda')

        if ausenciaId is not None:
            ausencia = Ausencia.objects.get(pk=ausenciaId)
            start_day = ausencia.start_day
            end_day = ausencia.end_day
            profesionalId = ausencia.profesional_id
        elif agendaId is not None:
            agenda = Agenda.objects.get(pk=agendaId)
            start_day = agenda.validFrom
            end_day = agenda.validTo
            profesionalId = agenda.profesional_id
        else:
            print 'Handle error'

        queryset = queryset.filter(day__range=(start_day,
                                               end_day),
                                   taken=True,
                                   status=Turno.STATUS_INACTIVE,
                                   profesional_id=profesionalId)

        return queryset
