from practicioners.models import PracticionerRolePeriod
from practicioners.serializers import PracticionerRolePeriodSerializer
from rest_framework import generics
from rest_framework.permissions import AllowAny

class PracticionerRolePeriodList(generics.ListCreateAPIView):
    """
    Crea un nuevo PracticionerRolePeriod, o lista los existentes
    :param request: En caso de creacion, la representacion json del PracticionerRolePeriod.
    :return: En caso de GET, la representacion json de un PracticionerRolePeriod.
    """
    serializer_class = PracticionerRolePeriodSerializer
    queryset = PracticionerRolePeriod.objects.all()
    permission_classes = (AllowAny,)
    paginate_by = 20

    def get_queryset(self):
        """
        Filtrado opcional del query, en base a un start y end dado
        """
        queryset = PracticionerRolePeriod.objects.all()
        start = self.request.query_params.get('start')
        end = self.request.query_params.get('end')

        if start is not None:
            queryset = queryset.filter(start=start)
        if end is not None:
            queryset = queryset.filter(end=end)
        return queryset

class PracticionerRolePeriodDetails(generics.RetrieveUpdateDestroyAPIView):
    """
    Devuelve, modifica o elimina una instancia de PracticionerRolePeriod
    :param request: En el caso de GET o DELETE, el pk del PracticionerRolePeriod como parte de la URL. En el caso de PUT, ademas, un objeto json representando el PracticionerRolePeriod
    :param pk: El primary key del PracticionerRolePeriod
    :return: En el caso de GET y PUT, una representacion de PracticionerRolePeriod
    """
    serializer_class = PracticionerRolePeriodSerializer
    queryset = PracticionerRolePeriod.objects.all()
    permission_classes = (AllowAny,)

    def get(self, request, *args, **kwargs):
        return generics.RetrieveUpdateDestroyAPIView.get(self, request, *args, **kwargs)