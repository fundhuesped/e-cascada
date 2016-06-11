#!/usr/bin/python
# -*- coding: utf-8 -*-

from rest_framework import generics
from rest_framework.permissions import AllowAny
from hc_common.serializers import EducationTypeNestSerializer
from hc_common.models import EducationType
from hc_core.views import PaginateListCreateAPIView


class EducationTypeList(PaginateListCreateAPIView):
    serializer_class = EducationTypeNestSerializer
    queryset = EducationType.objects.all()

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
    serializer_class = EducationTypeNestSerializer
    queryset = EducationType.objects.all()
    #permission_classes = (AllowAny,)
