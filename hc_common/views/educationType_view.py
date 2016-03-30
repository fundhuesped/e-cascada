#!/usr/bin/python
# -*- coding: utf-8 -*-

from rest_framework import generics
from rest_framework.permissions import AllowAny
from hc_common.serializers import EducationTypeSerializer
from hc_common.models import EducationType


class EducationTypeList(generics.ListCreateAPIView):
    serializer_class = EducationTypeSerializer
    queryset = EducationType.objects.all()
    permission_classes = (AllowAny,)
    paginate_by = 5


class EducationTypeDetails(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = EducationTypeSerializer
    queryset = EducationType.objects.all()
    permission_classes = (AllowAny,)
