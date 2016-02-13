from rest_framework import generics
from rest_framework.permissions import AllowAny
from common.serializers import PersonSerializer
from common.models import Person

class PersonList(generics.ListCreateAPIView):
    """
    Vista para listar Address existentes, o crear un nuevo Address
    """
    serializer_class = PersonSerializer
    queryset = Person.objects.all()
    permission_classes = (AllowAny,)
    paginate_by = 20

    def get_queryset(self):
        """
        Búsqueda opcional de Address, en base a un first_name o last_name
        :return:
        """
        queryset = Person.objects.all()
        first_name = self.request.query_params.get('first_name')
        last_name = self.request.query_params.get('last_name')

        if first_name is not None:
            queryset = queryset.filter(name__given__istartswith=first_name)
        if last_name is not None:
            queryset = queryset.filter(name__family__istartswith=last_name)


class PersonDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Vista para ver del detalle, modificar, o eliminar un Person
    """
    serializer_class = PersonSerializer
    queryset = Person.objects.all()
    permission_classes = (AllowAny,)