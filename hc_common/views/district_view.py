#!/usr/bin/python
# -*- coding: utf-8 -*-

from rest_framework import generics
from rest_framework.permissions import AllowAny
from hc_common.serializers import DistrictNestSerializer
from hc_common.models import District


class DistrictList(generics.ListCreateAPIView):
    serializer_class = DistrictNestSerializer
    queryset = District.objects.all()
    permission_classes = (AllowAny,)
    paginate_by = 5


class DistrictDetails(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = DistrictNestSerializer
    queryset = District.objects.all()
    permission_classes = (AllowAny,)
