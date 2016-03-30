#!/usr/bin/python
# -*- coding: utf-8 -*-

from rest_framework import generics
from rest_framework.permissions import AllowAny
from hc_common.serializers import LocationNestSerializer
from hc_common.models import Location


class LocationList(generics.ListCreateAPIView):
    serializer_class = LocationNestSerializer
    queryset = Location.objects.all()
    permission_classes = (AllowAny,)
    paginate_by = 5


class LocationDetails(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = LocationNestSerializer
    queryset = Location.objects.all()
    permission_classes = (AllowAny,)
