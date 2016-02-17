#!/usr/bin/python
# -*- coding: utf-8 -*-

from rest_framework import generics
from rest_framework.permissions import AllowAny
from common.serializers import DayOfWeekSerializer
from common.models import DayOfWeek


class DayOfWeekList(generics.ListCreateAPIView):
    """
    Crea un nuevo DayOfWeek, o lista los existentes.
    :param request: En caso de creacion, la representacion json del DayOfWeek.
    :return: En caso de GET, la representacion json de un DayOfWeek.
    """
    serializer_class = DayOfWeekSerializer
    queryset = DayOfWeek.objects.all()
    permission_classes = (AllowAny,)
    paginate_by = 7

class DayOfWeekDetails(generics.RetrieveUpdateDestroyAPIView):
    """
    Devuelve, modifica o elimina una instancia de DayOfWeek
    :param request: En el caso de GET o DELETE, el pk del DayOfWeek como parte de la URL. En el caso de PUT, ademas, un objeto json representando el DayOfWeek
    :param pk: El primary key del DayOfWeek
    :return: En el caso de GET y PUT, una representacion de DayOfWeek
    """
    serializer_class = DayOfWeekSerializer
    queryset = DayOfWeek.objects.all()
    permission_classes = (AllowAny,)

    def get(self, request, *args, **kwargs):
        return generics.RetrieveUpdateDestroyAPIView.get(self, request, *args, **kwargs)