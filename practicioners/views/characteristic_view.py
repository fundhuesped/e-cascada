from rest_framework import generics
from rest_framework.permissions import AllowAny
from practicioners.serializers import CharacteristicSerializer
from practicioners.models import Characteristic

class CharacteristicList(generics.ListCreateAPIView):
    """
    Vista para listar Characteristic existentes, o crear un nuevo ServiceCategory
    """
    serializer_class = CharacteristicSerializer
    queryset = Characteristic.objects.all()
    permission_classes = (AllowAny,)
    paginate_by = 20

class CharacteristicDetails(generics.RetrieveUpdateDestroyAPIView):
    """
    Vista para ver del detalle, modificar, o eliminar un Characteristic
    """
    serializer_class = CharacteristicSerializer
    queryset = Characteristic.objects.all()
    permission_classes = (AllowAny,)