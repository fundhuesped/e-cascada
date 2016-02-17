#!/usr/bin/python
# -*- coding: utf-8 -*-

from rest_framework import generics
from rest_framework.permissions import AllowAny
from common.serializers import AddressLineSerializer, AddressPointPeriodSerializer, AddressSerializer
from common.models import AddressLine, AddressPointPeriod, Address
from datetime import datetime

class AddressList(generics.ListCreateAPIView):
    """
    Vista para listar Address existentes, o crear un nuevo Address
    """
    serializer_class = AddressSerializer
    queryset = Address.objects.all()
    permission_classes = (AllowAny,)
    paginate_by = 20

    def get_queryset(self):
        """
        Bsqueda opcional de Address, en base a use, type, city, district, state, postalCode o country
        :return:
        """
        queryset = Address.objects.all()
        use = self.request.query_params.get('use')
        type = self.request.query_params.get('type')
        city = self.request.query_params.get('city')
        district = self.request.query_params.get('district')
        state = self.request.query_params.get('state')
        postalCode = self.request.query_params.get('postalcode')
        country = self.request.query_params.get('country')
        active = self.request.query_params.get('active')

        if use is not None:
            queryset = queryset.filter(use=use)
        if type is not None:
            queryset = queryset.filter(type=type)
        if city is not None:
            queryset = queryset.filter(city=city)
        if district is not None:
            queryset = queryset.filter(district=district)
        if state is not None:
            queryset = queryset.filter(state=state)
        if postalCode is not None:
            queryset = queryset.filter(postalCode=postalCode)
        if country is not None:
            queryset = queryset.filter(country=country)

class AddressDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Vista para ver del detalle, modificar, o eliminar un Address
    """
    serializer_class = AddressSerializer
    queryset = Address.objects.all()
    permission_classes = (AllowAny,)
