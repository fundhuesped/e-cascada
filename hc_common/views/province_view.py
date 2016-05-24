#!/usr/bin/python
# -*- coding: utf-8 -*-

from rest_framework import generics
from rest_framework.permissions import AllowAny
from hc_common.serializers import ProvinceNestSerializer
from hc_common.models import Province


class ProvinceList(generics.ListCreateAPIView):
    serializer_class = ProvinceNestSerializer
    queryset = Province.objects.all()
    #permission_classes = (AllowAny,)

    def get_queryset(self):
        queryset = Province.objects.all()
        name = self.request.query_params.get('name')
        status = self.request.query_params.get('status')
        if name is not None:
            queryset = queryset.filter(name__startswith=name)
        if status is not None:
            queryset = queryset.filter(status=status)
        return queryset


class ProvinceDetails(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ProvinceNestSerializer
    queryset = Province.objects.all()
    #permission_classes = (AllowAny,)
