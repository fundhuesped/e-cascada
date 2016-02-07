from rest_framework import generics
from rest_framework.permissions import AllowAny
from common.models import NamePeriod, HumanName
from common.serializers import NamePeriodSerializer, HumanNameSerializer

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


class NamePeriodList(generics.ListCreateAPIView):
    """
    Crea un nuevo NamePeriod, o lista los existentes
    :param request: En caso de creacion, la representacion json del NamePeriod.
    :return: En caso de GET, la representacion json de un NamePeriod.
    """
    serializer_class = NamePeriodSerializer
    queryset = NamePeriod.objects.all()
    permission_classes = (AllowAny,)
    paginate_by = 100

    def get_queryset(self):
        """
        Filtrado opcional del query, en base a un NamePeriod dado
        """
        queryset = NamePeriod.objects.all()
        start = self.request.query_params.get('start')
        end = self.request.query_params.get('end')

        if start is not None:
            queryset = queryset.filter(start=start)
        if end is not None:
            queryset = queryset.filter(end=end)
        return queryset

class NamePeriodDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Devuelve, modifica o elimina una instancia de NamePeriod
    :param request: En el caso de GET o DELETE, el pk del NamePeriod como parte de la URL. En el caso de PUT, ademas, un objeto json representando el NamePeriod
    :param pk: El primary key del NamePeriod
    :return: En el caso de GET y PUT, una representacion de NamePeriod
    """
    serializer_class = NamePeriodSerializer
    queryset = NamePeriod.objects.all()
    permission_classes = (AllowAny,)

    def get(self, request, *args, **kwargs):
        return generics.RetrieveUpdateDestroyAPIView.get(self, request, *args, **kwargs)

