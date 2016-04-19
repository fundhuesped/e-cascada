#!/usr/bin/python
# -*- coding: utf-8 -*-

from rest_framework import generics
from rest_framework.permissions import AllowAny
from hc_practicas.serializers import DayOfWeekNestSerializer
from hc_practicas.models import DayOfWeek


class DayOfWeekList(generics.ListCreateAPIView):
    serializer_class = DayOfWeekNestSerializer
    queryset = DayOfWeek.objects.all()
    permission_classes = (AllowAny,)
    paginate_by = 20


class DayOfWeekDetails(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = DayOfWeekNestSerializer
    queryset = DayOfWeek.objects.all()
    permission_classes = (AllowAny,)
