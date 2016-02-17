#!/usr/bin/python
# -*- coding: utf-8 -*-

from rest_framework import generics
from rest_framework.permissions import AllowAny
from practicioners.serializers import ReferralMethodSerializer
from practicioners.models import ReferralMethod

class ReferralMethodList(generics.ListCreateAPIView):
    """
    Vista para listar ReferralMethod existentes, o crear un nuevo ReferralMethod
    """
    serializer_class = ReferralMethodSerializer
    queryset = ReferralMethod.objects.all()
    permission_classes = (AllowAny,)
    paginate_by = 20

class ReferralMethodDetails(generics.RetrieveUpdateDestroyAPIView):
    """
    Vista para ver del detalle, modificar, o eliminar un ReferralMethod
    """
    serializer_class = ReferralMethodSerializer
    queryset = ReferralMethod.objects.all()
    permission_classes = (AllowAny,)