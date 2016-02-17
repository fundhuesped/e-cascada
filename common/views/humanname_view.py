#!/usr/bin/python
# -*- coding: utf-8 -*-

from rest_framework import generics
from rest_framework.permissions import AllowAny
from common.models import HumanName
from common.serializers import HumanNameSerializer

class HumanNameList(generics.ListCreateAPIView):
    model = HumanName
    serializer_class = HumanNameSerializer
    permission_classes = (AllowAny,)
    queryset = HumanName.objects.all()

    def get_queryset(self):
        """
        filtrado opcional del query, en base a family y given
        :return:
        """
        queryset = HumanName.objects.all()
        family = self.request.query_params.get('family')
        given = self.request.query_params.get('given')

        if family is not None:
            queryset = queryset.filter(family=family)
        if given is not None:
            queryset = queryset.filter(given=given)
        return queryset

class HumanNameDetails(generics.RetrieveUpdateDestroyAPIView):
    """
    Devuelve, modifica o elimina una instancia de HumanName
    """
    serializer_class = HumanNameSerializer
    queryset = HumanName.objects.all()
    permission_classes = (AllowAny,)

