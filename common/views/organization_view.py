#!/usr/bin/python
# -*- coding: utf-8 -*-

from rest_framework import generics
from rest_framework.permissions import AllowAny
from common.models import Organization
from common.serializers import OrganizationSerializer

class OrganizationList(generics.ListCreateAPIView):
    """
    Crea un nuevo Organization, o lista los existentes
    :param request: En caso de creacion, la representacion json del Organization.
    :return: En caso de GET, la representacion json de un Organization.
    """
    serializer_class = OrganizationSerializer
    queryset = Organization.objects.all()
    permission_classes = (AllowAny,)
    paginate_by = 100

    def get_queryset(self):
        """
        Filtrado opcional del query, en base a un type and name dados
        """
        queryset = Organization.objects.all()
        type = self.request.query_params.get('type')
        name = self.request.query_params.get('name')

        if type is not None:
            queryset = queryset.filter(type=type)
        if name is not None:
            queryset = queryset.filter(name=name)
        return queryset

class OrganizationDetails(generics.RetrieveUpdateDestroyAPIView):
    """
    Devuelve, modifica o elimina una instancia de Organization
    :param request: En el caso de GET o DELETE, el pk del Organization como parte de la URL. En el caso de PUT, ademas, un objeto json representando el Organization
    :param pk: El primary key del Organization
    :return: En el caso de GET y PUT, una representacion de Organization
    """
    serializer_class = OrganizationSerializer
    queryset = Organization.objects.all()
    permission_classes = (AllowAny,)

    def get(self, request, *args, **kwargs):
        return generics.RetrieveUpdateDestroyAPIView.get(self, request, *args, **kwargs)