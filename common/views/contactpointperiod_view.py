from common.models import ContactPointPeriod
from common.serializers import ContactPointPeriodSerializer
from rest_framework import generics
from rest_framework.permissions import AllowAny

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