#!/usr/bin/python
# -*- coding: utf-8 -*-

from rest_framework import generics
from rest_framework.permissions import AllowAny
from hc_common.serializers import SocialServiceSerializer
from hc_common.models import SocialService


class SocialServiceList(generics.ListCreateAPIView):
    serializer_class = SocialServiceSerializer
    queryset = SocialService.objects.all()
    permission_classes = (AllowAny,)
    paginate_by = 5


class SocialServiceDetails(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = SocialServiceSerializer
    queryset = SocialService.objects.all()
    permission_classes = (AllowAny,)
