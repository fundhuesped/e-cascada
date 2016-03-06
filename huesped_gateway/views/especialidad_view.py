#!/usr/bin/python
# -*- coding: utf-8 -*-

from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from huesped_gateway.serializers import EspecialidadSerializer
from huesped_gateway.models import Especialidad
from ..config_base_model import GatewayBaseModel

class EspecialidadList(generics.ListCreateAPIView):
    """
    Vista para listar Especialidades existentes, o crear una nueva Especialidad
    """
    serializer_class = EspecialidadSerializer
    name_map = {'serviceName':'name', 'comment':'description', 'id':'id'}
    queryset = Especialidad.objects.raw('SELECT * FROM practicioners_healthcareservice', translations=name_map)
    permission_classes = (AllowAny,)
    paginate_by = 20

    def get_queryset(self):
        """
        Filtrado opcional del query, en base a name (valida que comience con los datos dados)
        """
        name_map = {'serviceName':'name', 'comment':'description', 'id':'id'}
        query = 'SELECT * FROM practicioners_healthcareservice'
        name = self.request.query_params.get('name')
        if name is not None:
            query = query+' WHERE serviceName=\'' + name + '\''
        queryset = Especialidad.objects.raw(query, translations=name_map)

        return queryset

    def perform_create(self, serializer):
        """
        Override de la creación de especialidad, para mapear contra HealthcareService
        :param serializer:
        :return:
        """
        gbm = GatewayBaseModel()
        gbm.createHealthCareService(serializer.validated_data['name'], serializer.validated_data['description'])
        serializer.save()


class EspecialidadDetails(generics.RetrieveUpdateDestroyAPIView):
    """
    Vista para ver del detalle, modificar, o eliminar una Especialidad
    """
    serializer_class = EspecialidadSerializer
    name_map = {'serviceName':'name', 'comment':'description', 'id':'id'}
    queryset = Especialidad.objects.raw('SELECT * FROM practicioners_healthcareservice', translations=name_map)
    #queryset = Especialidad.objects.all()
    permission_classes = (AllowAny,)

    def delete(self, request, *args, **kwargs):
        super.delete(self, request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        super.get(self, request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        super.update(self, request, *args, **kwargs)

