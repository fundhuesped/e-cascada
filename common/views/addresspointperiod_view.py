from rest_framework import generics
from rest_framework.permissions import AllowAny
from common.serializers import AddressPointPeriodSerializer
from common.models import AddressPointPeriod

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