#!/usr/bin/python
# -*- coding: utf-8 -*-

from rest_framework import generics
from rest_framework.permissions import AllowAny
from hc_common.serializers import ProvinceSerializer
from hc_common.models import Province


class ProvinceList(generics.ListCreateAPIView):
    serializer_class = ProvinceSerializer
    queryset = Province.objects.all()
    permission_classes = (AllowAny,)
    paginate_by = 5


class ProvinceDetails(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ProvinceSerializer
    queryset = Province.objects.all()
    permission_classes = (AllowAny,)
