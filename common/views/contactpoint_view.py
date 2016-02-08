from common.models import ContactPoint
from common.serializers import ContactPointSerializer
from rest_framework import generics
from rest_framework.permissions import AllowAny

class ContactPointList(generics.ListCreateAPIView):
    model = ContactPoint
    serializer_class = ContactPointSerializer
    permission_classes = (AllowAny,)
    queryset = ContactPoint.objects.all()

class ContactPointDetails(generics.RetrieveUpdateDestroyAPIView):
    """
    Devuelve, modifica o elimina una instancia de ContactPoint
    """
    serializer_class = ContactPointSerializer
    queryset = ContactPoint.objects.all()
    permission_classes = (AllowAny,)



