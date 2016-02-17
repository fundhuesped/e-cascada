#!/usr/bin/python
# -*- coding: utf-8 -*-

from rest_framework import generics
from rest_framework.permissions import AllowAny
from common.serializers import IdentifierSerializer
from common.models import Identifier

class IdentifierList(generics.ListCreateAPIView):
    """
    Crea un nuevo Identifier, o lista los existentes
    :param request: En caso de creacion, la representacion json del Identifier.
    :return: En caso de GET, la representacion json de un Identifier.
    """
    serializer_class = IdentifierSerializer
    queryset = Identifier.objects.all()
    permission_classes = (AllowAny,)
    paginate_by = 20

    def get_queryset(self):
        """
        Filtrado opcional del query, en base a un system o type dado
        """
        queryset = Identifier.objects.all()
        system = self.request.query_params.get('system')
        type = self.request.query_params.get('type')

        if system is not None:
            queryset = queryset.filter(system=system)
        if type is not None:
            queryset = queryset.filter(type=type)
        return queryset

class IdentifierDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Devuelve, modifica o elimina una instancia de Identifier
    :param request: En el caso de GET o DELETE, el pk del Identifier como parte de la URL. En el caso de PUT, ademas, un objeto json representando el Identifier
    :param pk: El primary key del Identifier
    :return: En el caso de GET y PUT, una representacion de Identifier
    """
    serializer_class = IdentifierSerializer
    queryset = Identifier.objects.all()
    permission_classes = (AllowAny,)

    def get(self, request, *args, **kwargs):
        return generics.RetrieveUpdateDestroyAPIView.get(self, request, *args, **kwargs)

