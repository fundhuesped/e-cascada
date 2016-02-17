#!/usr/bin/python
# -*- coding: utf-8 -*-

from rest_framework import generics
from rest_framework.permissions import AllowAny
from practicioners.serializers import HealthCareServiceSerializer
from practicioners.models import HealthcareService

class HealthCareServiceList(generics.ListCreateAPIView):
    """
    Vista para listar Eligibility existentes, o crear un nuevo ServiceCategory
    """
    serializer_class = HealthCareServiceSerializer
    queryset = HealthcareService.objects.all()
    permission_classes = (AllowAny,)
    paginate_by = 20

    def get_queryset(self):
        """
        Devuelve HealthcareService filtrado por serviceName
        :return:
        """
        queryset = HealthcareService.objects.all()
        serviceName = self.request.query_params.get('serviceName')
        if serviceName is not None:
            queryset = queryset.filter(serviceName=serviceName)

class HealthCareServiceDetails(generics.RetrieveUpdateDestroyAPIView):
    """
    Vista para ver del detalle, modificar, o eliminar un Eligibility
    """
    serializer_class = HealthCareServiceSerializer
    queryset = HealthcareService.objects.all()
    permission_classes = (AllowAny,)