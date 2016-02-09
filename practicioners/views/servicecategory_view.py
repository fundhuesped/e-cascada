from rest_framework import generics
from rest_framework.permissions import AllowAny
from practicioners.serializers import ServiceCategorySerializer
from practicioners.models import ServiceCategory

class ServiceCategoryList(generics.ListCreateAPIView):
    """
    Vista para listar ServiceCategory existentes, o crear un nuevo ServiceCategory
    """
    serializer_class = ServiceCategorySerializer
    queryset = ServiceCategory.objects.all()
    permission_classes = (AllowAny,)
    paginate_by = 20

class ServiceCategoryDetails(generics.RetrieveUpdateDestroyAPIView):
    """
    Vista para ver del detalle, modificar, o eliminar un ServiceCategory
    """
    serializer_class = ServiceCategorySerializer
    queryset = ServiceCategory.objects.all()
    permission_classes = (AllowAny,)