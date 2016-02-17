#!/usr/bin/python
# -*- coding: utf-8 -*-

from rest_framework import generics
from rest_framework.permissions import AllowAny
from common.models import OrganizationContact
from common.serializers import OrganizationContactSerializer

class OrganizationContactList(generics.ListCreateAPIView):
    """
    Crea un nuevo OrganizationContact, o lista los existentes
    :param request: En caso de creacion, la representacion json del OrganizationContact.
    :return: En caso de GET, la representacion json de un OrganizationContact.
    """
    serializer_class = OrganizationContactSerializer
    queryset = OrganizationContact.objects.all()
    permission_classes = (AllowAny,)
    paginate_by = 100

    def get_queryset(self):
        """
        Filtrado opcional del query, en base a un purpose dado
        """
        queryset = OrganizationContact.objects.all()
        purpose = self.request.query_params.get('purpose')

        if purpose is not None:
            queryset = queryset.filter(purpose=purpose)
        return queryset

class OrganizationContactDetails(generics.RetrieveUpdateDestroyAPIView):
    """
    Devuelve, modifica o elimina una instancia de OrganizationContact
    :param request: En el caso de GET o DELETE, el pk del OrganizationContact como parte de la URL. En el caso de PUT, ademas, un objeto json representando el OrganizationContact
    :param pk: El primary key del OrganizationContact
    :return: En el caso de GET y PUT, una representacion de OrganizationContact
    """
    serializer_class = OrganizationContactSerializer
    queryset = OrganizationContact.objects.all()
    permission_classes = (AllowAny,)

    def get(self, request, *args, **kwargs):
        return generics.RetrieveUpdateDestroyAPIView.get(self, request, *args, **kwargs)