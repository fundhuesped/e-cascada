from rest_framework import generics
from rest_framework.permissions import AllowAny
from common.serializers import IdentifierPeriodSerializer
from common.models import IdentifierPeriod

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