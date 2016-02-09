from practicioners.models import NotAvailablePeriod
from practicioners.serializers import NotAvailablePeriodSerializer
from rest_framework import generics
from rest_framework.permissions import AllowAny

class NotAvailablePeriodList(generics.ListCreateAPIView):
    """
    Crea un nuevo NotAvailablePeriod, o lista los existentes
    :param request: En caso de creacion, la representacion json del NotAvailablePeriod.
    :return: En caso de GET, la representacion json de un NotAvailablePeriod.
    """
    serializer_class = NotAvailablePeriodSerializer
    queryset = NotAvailablePeriod.objects.all()
    permission_classes = (AllowAny,)
    paginate_by = 20

    def get_queryset(self):
        """
        Filtrado opcional del query, en base a un start y end dado
        """
        queryset = NotAvailablePeriod.objects.all()
        start = self.request.query_params.get('start')
        end = self.request.query_params.get('end')

        if start is not None:
            queryset = queryset.filter(start=start)
        if end is not None:
            queryset = queryset.filter(end=end)
        return queryset

class NotAvailablePeriodDetails(generics.RetrieveUpdateDestroyAPIView):
    """
    Devuelve, modifica o elimina una instancia de NotAvailablePeriod
    :param request: En el caso de GET o DELETE, el pk del NotAvailablePeriod como parte de la URL. En el caso de PUT, ademas, un objeto json representando el NotAvailablePeriod
    :param pk: El primary key del NotAvailablePeriod
    :return: En el caso de GET y PUT, una representacion de NotAvailablePeriod
    """
    serializer_class = NotAvailablePeriodSerializer
    queryset = NotAvailablePeriod.objects.all()
    permission_classes = (AllowAny,)

    def get(self, request, *args, **kwargs):
        return generics.RetrieveUpdateDestroyAPIView.get(self, request, *args, **kwargs)