from rest_framework import generics
from rest_framework.permissions import AllowAny
from common.serializers import PersonLinkSerializer
from common.models import PersonLink

class PersonLinkList(generics.ListCreateAPIView):
    """
    Vista para listar PersonLin existentes, o crear un nuevo PersonLin
    """
    serializer_class = PersonLinkSerializer
    queryset = PersonLink.objects.all()
    permission_classes = (AllowAny,)
    paginate_by = 20


class PersonLinkDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Vista para ver del detalle, modificar, o eliminar un PersonLink
    """
    serializer_class = PersonLinkSerializer
    queryset = PersonLink.objects.all()
    permission_classes = (AllowAny,)