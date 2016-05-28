#!/usr/bin/python
# -*- coding: utf-8 -*-

from rest_framework import generics
from rest_framework.permissions import AllowAny
from hc_common.serializers import CivilStatusTypeNestSerializer
from hc_common.models import CivilStatusType
from hc_core.views.paginateListCreateAPIView import PaginateListCreateAPIView

class CivilStatusTypeList(PaginateListCreateAPIView):
    serializer_class = CivilStatusTypeNestSerializer
    queryset = CivilStatusType.objects.all()

    def get_queryset(self):
        queryset = CivilStatusType.objects.all()
        name = self.request.query_params.get('name')
        status = self.request.query_params.get('status')

        if name is not None:
            queryset = queryset.filter(name__startswith=name)
        if status is not None:
            queryset = queryset.filter(status=status)

        return queryset


class CivilStatusTypeDetails(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CivilStatusTypeNestSerializer
    queryset = CivilStatusType.objects.all()
