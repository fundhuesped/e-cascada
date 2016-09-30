#!/usr/bin/python
# -*- coding: utf-8 -*-

from hc_core.views import PaginateListCreateAPIView
from hc_practicas.models import Period
from hc_practicas.serializers import PeriodNestSerializer
from rest_framework import filters
from rest_framework import generics


class PeriodList(PaginateListCreateAPIView):
    serializer_class = PeriodNestSerializer
    queryset = Period.objects.all()
    filter_backends = (filters.OrderingFilter,)


class PeriodDetails(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = PeriodNestSerializer
    queryset = Period.objects.all()
