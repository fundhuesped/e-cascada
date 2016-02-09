from rest_framework import generics
from rest_framework.permissions import AllowAny
from practicioners.serializers import EligibilitySerializer
from practicioners.models import Eligibility

class EligibilityList(generics.ListCreateAPIView):
    """
    Vista para listar Eligibility existentes, o crear un nuevo ServiceCategory
    """
    serializer_class = EligibilitySerializer
    queryset = Eligibility.objects.all()
    permission_classes = (AllowAny,)
    paginate_by = 20

class EligibilityDetails(generics.RetrieveUpdateDestroyAPIView):
    """
    Vista para ver del detalle, modificar, o eliminar un Eligibility
    """
    serializer_class = EligibilitySerializer
    queryset = Eligibility.objects.all()
    permission_classes = (AllowAny,)