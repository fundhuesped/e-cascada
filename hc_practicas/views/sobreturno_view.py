#!/usr/bin/python
# -*- coding: utf-8 -*-

from hc_practicas.models import Agenda
from hc_practicas.models import Ausencia
from hc_practicas.models import Turno
from hc_practicas.serializers import SobreturnoNestSerializer
from rest_framework import filters
from rest_framework import generics

from rest_framework.response import Response
from rest_framework import status

class SobreturnoCreate(generics.CreateAPIView):
    serializer_class = SobreturnoNestSerializer

    # def create(self, request, *args, **kwargs):
    #     serializer = self.get_serializer(data=request.data)
    #     serializer.is_valid(raise_exception=True)
    #     self.perform_create(serializer)
    #     headers = self.get_success_headers(serializer.data)
    #     return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)