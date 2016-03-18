#!/usr/bin/python
# -*- coding: utf-8 -*-

from rest_framework import generics
from rest_framework.permissions import AllowAny
from hc_common.serializers import PersonaSerializer
from hc_common.models import Persona

class PersonaList(generics.ListCreateAPIView):
    """
    Vista para listar Personas existentes, o crear una nueva Persona
    """
    serializer_class = PersonaSerializer
    queryset = Persona.objects.all()
    permission_classes = (AllowAny,)
    paginate_by = 20

    def get_queryset(self):
        """
        Filtrado del queryset por nombre y primer apellido, si como mínimo tienen 3 caracteres
        :return:
        """
        queryset = Persona.objects.all()
        firstName = self.request.query_params.get('firstName')
        fatherSurename = self.request.query_params.get('fatherSurename')

        if (firstName is not None and len(firstName)>3):
            queryset = queryset.filter(firstName__startswith=firstName)

        if (fatherSurename is not None and len(fatherSurename)>3):
            queryset = queryset.filter(fatherSurename__startswith=fatherSurename)

        return queryset

class PersonaDetails(generics.RetrieveUpdateDestroyAPIView):
    """
    Vista para ver del detalle, modificar, o eliminar un Documento
    """
    serializer_class = PersonaSerializer
    queryset = Persona.objects.all()
    permission_classes = (AllowAny,)