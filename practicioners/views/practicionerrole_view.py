from practicioners.models import PracticionerRole
from practicioners.serializers import PracticionerRoleSerializer
from rest_framework import generics
from rest_framework.permissions import AllowAny

class PracticionerRoleList(generics.ListCreateAPIView):
    model = PracticionerRole
    serializer_class = PracticionerRoleSerializer
    permission_classes = (AllowAny,)
    queryset = PracticionerRole.objects.all()

class PracticionerRoleDetails(generics.RetrieveUpdateDestroyAPIView):
    """
    Devuelve, modifica o elimina una instancia de PracticionerRole
    """
    serializer_class = PracticionerRoleSerializer
    queryset = PracticionerRole.objects.all()
    permission_classes = (AllowAny,)