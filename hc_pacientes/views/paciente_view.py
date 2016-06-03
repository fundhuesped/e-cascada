#!/usr/bin/python
# -*- coding: utf-8 -*-

from rest_framework import generics
from rest_framework.permissions import AllowAny
from hc_pacientes.serializers import PacienteNestSerializer
from hc_pacientes.models import Paciente
from hc_core.views import PaginateListCreateAPIView


class PacienteList(PaginateListCreateAPIView):
    """
    Vista para listar Pacientes existentes, o crear un nuevo Paciente
    """
    serializer_class = PacienteNestSerializer
    queryset = Paciente.objects.all()

    def get_queryset(self):
        queryset = Paciente.objects.all()
        firstName = self.request.query_params.get('firstName')
        fatherSurname = self.request.query_params.get('fatherSurname')
        status = self.request.query_params.get('status')
        documentType = self.request.query_params.get('documentType')
        document = self.request.query_params.get('documentNumber')
        if firstName is not None and len(firstName) >= 3:
            queryset = queryset.filter(firstName__startswith=firstName)
        if fatherSurname is not None and len(fatherSurname) >= 3:
            queryset = queryset.filter(fatherSurname__startswith=fatherSurname)
        if status is not None:
            queryset = queryset.filter(status=status)
        if documentType is not None:
            queryset = queryset.filter(documentType=documentType)
        if document is not None:
            queryset = queryset.filter(documentNumber=document)
        #Order  
        order_field = self.request.query_params.get('order_field')
        order_by = self.request.query_params.get('order_by')
        if (order_field is not None) and (order_by is not None):
            if order_by == 'asc':
                queryset = queryset.order_by(order_field)
            else:
                if order_by == 'desc':
                    queryset = queryset.order_by('-'+order_field)
        return queryset


class PacienteDetails(generics.RetrieveUpdateDestroyAPIView):
    """
    Vista para ver del detalle, modificar, o eliminar un paciente
    """
    serializer_class = PacienteNestSerializer
    queryset = Paciente.objects.all()
    permission_classes = (AllowAny,)
