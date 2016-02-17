from rest_framework import generics
from rest_framework.permissions import AllowAny
from common.serializers import LocationSerializer
from common.models import Location

class LocationList(generics.ListCreateAPIView):
    """
    Vista para listar Location existentes, o crear un nuevo Address
    """
    serializer_class = LocationSerializer
    queryset = Location.objects.all()
    permission_classes = (AllowAny,)
    paginate_by = 20

    def get_queryset(self):
        """
        Bsqueda opcional de Location, en base a name, type
        :return:
        """
        queryset = Location.objects.all()
        name = self.request.query_params.get('name')
        type = self.request.query_params.get('type')

        if name is not None:
            queryset = queryset.filter(use=name)
        if type is not None:
            queryset = queryset.filter(type=type)

        return queryset

class LocationDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Vista para ver del detalle, modificar, o eliminar un Location
    """
    serializer_class = LocationSerializer
    queryset = Location.objects.all()
    permission_classes = (AllowAny,)
