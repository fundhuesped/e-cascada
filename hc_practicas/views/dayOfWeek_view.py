#!/usr/bin/python
# -*- coding: utf-8 -*-

from rest_framework import generics, filters
from rest_framework.permissions import AllowAny
from hc_practicas.serializers import DayOfWeekNestSerializer
from hc_practicas.models import DayOfWeek
from hc_core.views import PaginateListCreateAPIView

class DayOfWeekList(PaginateListCreateAPIView):
    serializer_class = DayOfWeekNestSerializer
    queryset = DayOfWeek.objects.all()
    filter_backends = (filters.OrderingFilter,)

class DayOfWeekDetails(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = DayOfWeekNestSerializer
    queryset = DayOfWeek.objects.all()
    #permission_classes = (AllowAny,)
