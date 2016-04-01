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
    paginate_by = 20

    def get_queryset(self):
        queryset = EducationType.objects.all()
        name = self.request.query_params.get('name')
        status = self.request.query_params.get('status')
        if name is not None:
            queryset = queryset.filter(name__startswith=name)
        if status is not None:
            queryset = queryset.filter(status=status)
        return queryset


class EducationTypeDetails(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = EducationTypeSerializer
    queryset = EducationType.objects.all()
    permission_classes = (AllowAny,)
