#!/usr/bin/python
# -*- coding: utf-8 -*-

from rest_framework import generics
from rest_framework.permissions import AllowAny
from hc_common.serializers import AddressSerializer
from hc_common.models import Address


class AddressList(generics.ListCreateAPIView):
    serializer_class = AddressSerializer
    queryset = Address.objects.all()
    permission_classes = (AllowAny,)
    paginate_by = 5


class AddressDetails(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = AddressSerializer
    queryset = Address.objects.all()
    permission_classes = (AllowAny,)
