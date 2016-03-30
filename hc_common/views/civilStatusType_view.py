#!/usr/bin/python
# -*- coding: utf-8 -*-

from rest_framework import generics
from rest_framework.permissions import AllowAny
from hc_common.serializers import CivilStatusTypeSerializer
from hc_common.models import CivilStatusType


class CivilStatusTypeList(generics.ListCreateAPIView):
    serializer_class = CivilStatusTypeSerializer
    queryset = CivilStatusType.objects.all()
    permission_classes = (AllowAny,)
    paginate_by = 5


class CivilStatusTypeDetails(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CivilStatusTypeSerializer
    queryset = CivilStatusType.objects.all()
    permission_classes = (AllowAny,)
