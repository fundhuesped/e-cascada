#!/usr/bin/python
# -*- coding: utf-8 -*-

from rest_framework import generics
from rest_framework.permissions import AllowAny
from hc_common.serializers import LocationNestSerializer
from hc_common.models import Location


class LocationList(generics.ListCreateAPIView):
    serializer_class = LocationNestSerializer
    queryset = Location.objects.all()
    #permission_classes = (AllowAny,)

    def get_queryset(self):
        queryset = Location.objects.all()
        name = self.request.query_params.get('name')
        status = self.request.query_params.get('status')
        district = self.request.query_params.get('district')
        if name is not None:
            queryset = queryset.filter(name__startswith=name)
        if status is not None:
            queryset = queryset.filter(status=status)
        if district is not None:
            queryset = queryset.filter(district_id=district)
        return queryset


class LocationDetails(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = LocationNestSerializer
    queryset = Location.objects.all()
    #permission_classes = (AllowAny,)
