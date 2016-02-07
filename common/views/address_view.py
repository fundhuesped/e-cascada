from rest_framework import generics
from rest_framework.permissions import AllowAny
from common.serializers import AddressLineSerializer, AddressPointPeriodSerializer, AddressSerializer
from common.models import AddressLine, AddressPointPeriod, Address
from _datetime import datetime

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
        Búsqueda opcional de Address, en base a use, type, city, district, state, postalCode o country
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
