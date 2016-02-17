#!/usr/bin/python
# -*- coding: utf-8 -*-

from rest_framework import generics
from rest_framework.permissions import AllowAny
from common.serializers import AddressLineSerializer
from common.models import AddressLine


class AddressLineList(generics.ListCreateAPIView):
    """
    Crea un nuevo NamePeriod, o lista los existentes
    :param request: En caso de creacion, la representacion json del NamePeriod.
    :return: En caso de GET, la representacion json de un NamePeriod.
    """
    serializer_class = AddressLineSerializer
    queryset = AddressLine.objects.all()
    permission_classes = (AllowAny,)
    paginate_by = 100

class AddressLineDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Devuelve, modifica o elimina una instancia de AddressLine
    :param request: En el caso de GET o DELETE, el pk del AddressLine como parte de la URL. En el caso de PUT, ademas, un objeto json representando el AddressLine
    :param pk: El primary key del NamePeriod
    :return: En el caso de GET y PUT, una representacion de AddressLine
    """
    serializer_class = AddressLineSerializer
    queryset = AddressLine.objects.all()
    permission_classes = (AllowAny,)