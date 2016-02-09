from rest_framework import generics
from rest_framework.permissions import AllowAny
from practicioners.serializers import TypeServiceSerializer
from practicioners.models import TypeService

class TypeServiceList(generics.ListCreateAPIView):
    """
    Vista para listar TypeService existentes, o crear un nuevo TypeService
    """
    serializer_class = TypeServiceSerializer
    queryset = TypeService.objects.all()
    permission_classes = (AllowAny,)
    paginate_by = 20

class TypeServiceDetails(generics.RetrieveUpdateDestroyAPIView):
    """
    Vista para ver del detalle, modificar, o eliminar un TypeService
    """
    serializer_class = TypeServiceSerializer
    queryset = TypeService.objects.all()
    permission_classes = (AllowAny,)