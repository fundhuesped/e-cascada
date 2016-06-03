#!/usr/bin/python
# -*- coding: utf-8 -*-

from rest_framework import generics
from rest_framework.permissions import AllowAny
from hc_common.serializers import SocialServiceNestSerializer
from hc_common.models import SocialService
from hc_core.views import PaginateListCreateAPIView

class SocialServiceList(PaginateListCreateAPIView):
    serializer_class = SocialServiceNestSerializer
    queryset = SocialService.objects.all()

    def get_queryset(self):
        queryset = SocialService.objects.all()
        name = self.request.query_params.get('name')
        status = self.request.query_params.get('status')
        if name is not None:
            queryset = queryset.filter(name__startswith=name)
        if status is not None:
            queryset = queryset.filter(status=status)
        return queryset


class SocialServiceDetails(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = SocialServiceNestSerializer
    queryset = SocialService.objects.all()
    #permission_classes = (AllowAny,)
