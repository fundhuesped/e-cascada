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
    paginate_by = 20

    def get_queryset(self):
        queryset = District.objects.all()
        name = self.request.query_params.get('name')
        status = self.request.query_params.get('status')
        province = self.request.query_params.get('province')
        if name is not None:
            queryset = queryset.filter(name__startswith=name)
        if status is not None:
            queryset = queryset.filter(status=status)
        if province is not None:
            queryset = queryset.filter(province_id=province)
        return queryset


class DistrictDetails(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = DistrictNestSerializer
    queryset = District.objects.all()
    permission_classes = (AllowAny,)