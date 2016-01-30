from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny
from django.http import Http404
from common.models import Coding, IdentifierType, IdentifierPeriod, ContactPointPeriod, AddressPointPeriod
from common.serializers import CodingSerializer, IdentifierTypeSerializer, IdentifierPeriodSerializer, ContactPointPeriodSerializer, AddressPointPeriodSerializer

class CodingList(generics.ListCreateAPIView):
    """
    Crea un nuevo Coding, o lista los existentes.
    :param request: En caso de creacion, la representacion json del Coding.
    :return: En caso de GET, la representacion json de un Coding.
    """
    serializer_class = CodingSerializer
    queryset = Coding.objects.all()
    permission_classes = (AllowAny,)
    paginate_by = 100

    def get_queryset(self):
        """
        Filtrado opcional del query, en base a display o code
        """
        queryset = Coding.objects.all()
        display = self.request.query_params.get('display')
        code = self.request.query_params.get('code')

        if display is not None:
            queryset = queryset.filter(display=display)
        if code is not None:
            queryset = queryset.filter(code=code)
        return queryset

class CodingDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Devuelve, modifica o elimina una instancia de Coding
    :param request: En el caso de GET o DELETE, el pk del Coding como parte de la URL. En el caso de PUT, ademas, un objeto json representando el Coding
    :param pk: El primary key del Coding
    :return: En el caso de GET y PUT, una representacion de Coding
    """
    serializer_class = CodingSerializer
    queryset = Coding.objects.all()
    permission_classes = (AllowAny,)

    def get(self, request, *args, **kwargs):
        return generics.RetrieveUpdateDestroyAPIView.get(self, request, *args, **kwargs)

class IdentifierTypeList(generics.ListCreateAPIView):
    """
    Crea un nuevo IdentifierType, o lista los existentes
    :param request: En caso de creacion, la representacion json del IdentifierType.
    :return: En caso de GET, la representacion json de un IdentifierType.
    """
    serializer_class = IdentifierTypeSerializer
    queryset = IdentifierType.objects.all()
    permission_classes = (AllowAny,)
    paginate_by = 100

    def get_queryset(self):
        """
        Filtrado opcional del query, en base a un coding dado
        """
        queryset = IdentifierType.objects.all()
        coding = self.request.query_params.get('coding')

        if coding is not None:
            queryset = queryset.filter(coding=coding)
        return queryset

class IdentifierTypeDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Devuelve, modifica o elimina una instancia de IdentifierType
    :param request: En el caso de GET o DELETE, el pk del IdentifierType como parte de la URL. En el caso de PUT, ademas, un objeto json representando el IdentifierType
    :param pk: El primary key del IdentifierType
    :return: En el caso de GET y PUT, una representacion de IdentifierType
    """
    serializer_class = IdentifierTypeSerializer
    queryset = IdentifierType.objects.all()
    permission_classes = (AllowAny,)

    def get(self, request, *args, **kwargs):
        return generics.RetrieveUpdateDestroyAPIView.get(self, request, *args, **kwargs)

class IdentifierPeriodList(generics.ListCreateAPIView):
    """
    Crea un nuevo IdentifierPeriod, o lista los existentes
    :param request: En caso de creacion, la representacion json del IdentifierPeriod.
    :return: En caso de GET, la representacion json de un IdentifierPeriod.
    """
    serializer_class = IdentifierPeriodSerializer
    queryset = IdentifierPeriod.objects.all()
    permission_classes = (AllowAny,)
    paginate_by = 100

    def get_queryset(self):
        """
        Filtrado opcional del query, en base a un coding dado
        """
        queryset = IdentifierPeriod.objects.all()
        start = self.request.query_params.get('start')
        end = self.request.query_params.get('end')

        if start is not None:
            queryset = queryset.filter(start=start)
        if end is not None:
            queryset = queryset.filter(end=end)
        return queryset

class IdentifierPeriodDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Devuelve, modifica o elimina una instancia de IdentifierPeriod
    :param request: En el caso de GET o DELETE, el pk del IdentifierType como parte de la URL. En el caso de PUT, ademas, un objeto json representando el IdentifierPeriod
    :param pk: El primary key del IdentifierPeriod
    :return: En el caso de GET y PUT, una representacion de IdentifierPeriod
    """
    serializer_class = IdentifierPeriodSerializer
    queryset = IdentifierPeriod.objects.all()
    permission_classes = (AllowAny,)

    def get(self, request, *args, **kwargs):
        return generics.RetrieveUpdateDestroyAPIView.get(self, request, *args, **kwargs)

class ContactPointPeriodList(generics.ListCreateAPIView):
    """
    Crea un nuevo ContactPointPeriod, o lista los existentes
    :param request: En caso de creacion, la representacion json del ContactPointPeriod.
    :return: En caso de GET, la representacion json de un ContactPointPeriod.
    """
    serializer_class = ContactPointPeriodSerializer
    queryset = ContactPointPeriod.objects.all()
    permission_classes = (AllowAny,)
    paginate_by = 100

    def get_queryset(self):
        """
        Filtrado opcional del query, en base a un coding dado
        """
        queryset = ContactPointPeriod.objects.all()
        start = self.request.query_params.get('start')
        end = self.request.query_params.get('end')

        if start is not None:
            queryset = queryset.filter(start=start)
        if end is not None:
            queryset = queryset.filter(end=end)
        return queryset

class ContactPointPeriodDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Devuelve, modifica o elimina una instancia de ContactPointPeriod
    :param request: En el caso de GET o DELETE, el pk del ContactPointPeriod como parte de la URL. En el caso de PUT, ademas, un objeto json representando el ContactPointPeriod
    :param pk: El primary key del ContactPointPeriod
    :return: En el caso de GET y PUT, una representacion de ContactPointPeriod
    """
    serializer_class = ContactPointPeriodSerializer
    queryset = ContactPointPeriod.objects.all()
    permission_classes = (AllowAny,)

    def get(self, request, *args, **kwargs):
        return generics.RetrieveUpdateDestroyAPIView.get(self, request, *args, **kwargs)

class AddressPointPeriodList(generics.ListCreateAPIView):
    """
    Crea un nuevo AddressPointPeriod, o lista los existentes
    :param request: En caso de creacion, la representacion json del AddressPointPeriod.
    :return: En caso de GET, la representacion json de un AddressPointPeriod.
    """
    serializer_class = AddressPointPeriodSerializer
    queryset = AddressPointPeriod.objects.all()
    permission_classes = (AllowAny,)
    paginate_by = 100

    def get_queryset(self):
        """
        Filtrado opcional del query, en base a un AddressPointPeriod dado
        """
        queryset = AddressPointPeriod.objects.all()
        start = self.request.query_params.get('start')
        end = self.request.query_params.get('end')

        if start is not None:
            queryset = queryset.filter(start=start)
        if end is not None:
            queryset = queryset.filter(end=end)
        return queryset

class AddressPointPeriodDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Devuelve, modifica o elimina una instancia de AddressPointPeriod
    :param request: En el caso de GET o DELETE, el pk del AddressPointPeriod como parte de la URL. En el caso de PUT, ademas, un objeto json representando el AddressPointPeriod
    :param pk: El primary key del AddressPointPeriod
    :return: En el caso de GET y PUT, una representacion de AddressPointPeriod
    """
    serializer_class = AddressPointPeriodSerializer
    queryset = AddressPointPeriod.objects.all()
    permission_classes = (AllowAny,)

    def get(self, request, *args, **kwargs):
        return generics.RetrieveUpdateDestroyAPIView.get(self, request, *args, **kwargs)