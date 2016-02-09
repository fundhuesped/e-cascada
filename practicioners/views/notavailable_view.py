from practicioners.models import NotAvailable
from practicioners.serializers import NotAvailableSerializer
from rest_framework import generics
from rest_framework.permissions import AllowAny

class NotAvailableList(generics.ListCreateAPIView):
    model = NotAvailable
    serializer_class = NotAvailableSerializer
    permission_classes = (AllowAny,)
    queryset = NotAvailable.objects.all()

class NotAvailableDetails(generics.RetrieveUpdateDestroyAPIView):
    """
    Devuelve, modifica o elimina una instancia de NotAvailable
    """
    serializer_class = NotAvailableSerializer
    queryset = NotAvailable.objects.all()
    permission_classes = (AllowAny,)