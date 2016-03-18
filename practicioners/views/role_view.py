from rest_framework import generics
from rest_framework.permissions import AllowAny
from practicioners.serializers import RoleSerializer
from practicioners.models import Role

class RoleList(generics.ListCreateAPIView):
    """
    Vista para listar Roles existentes, o crear un nuevo Role
    """
    serializer_class = RoleSerializer
    queryset = Role.objects.all()
    permission_classes = (AllowAny,)
    paginate_by = 20

class RoleDetails(generics.RetrieveUpdateDestroyAPIView):
    """
    Vista para ver del detalle, modificar, o eliminar un Role
    """
    serializer_class = RoleSerializer
    queryset = Role.objects.all()
    permission_classes = (AllowAny,)