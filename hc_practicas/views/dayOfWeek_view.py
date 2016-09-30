#!/usr/bin/python
# -*- coding: utf-8 -*-

from hc_core.views import PaginateListCreateAPIView
from hc_practicas.models import DayOfWeek
from hc_practicas.serializers import DayOfWeekNestSerializer
from rest_framework import filters
from rest_framework import generics

class DayOfWeekList(PaginateListCreateAPIView):
    serializer_class = DayOfWeekNestSerializer
    queryset = DayOfWeek.objects.all()
    filter_backends = (filters.OrderingFilter,)

class DayOfWeekDetails(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = DayOfWeekNestSerializer
    queryset = DayOfWeek.objects.all()
