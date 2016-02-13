from rest_framework import generics
from rest_framework.permissions import AllowAny
from practicioners.serializers import AvailableTimeSerializer
from practicioners.models import AvailableTime
from common.models import DayOfWeek

class AvailableTimeList(generics.ListCreateAPIView):
    """
    Vista para listar AvailableTime existentes, o crear un nuevo Address
    """
    serializer_class = AvailableTimeSerializer
    queryset = AvailableTime.objects.all()
    permission_classes = (AllowAny,)
    paginate_by = 20

    def get_queryset(self):
        """
        Bsqueda opcional de AvailableTime, en base a allDay
        :return:
        """
        queryset = AvailableTime.objects.all()
        allDay = self.request.query_params.get('allDay')

        if allDay is not None:
            queryset = queryset.filter(allDay=allDay)
        return queryset

class AvailableTimeDetails(generics.RetrieveUpdateDestroyAPIView):
    """
    Vista para ver del detalle, modificar, o eliminar un AvailableTime
    """
    serializer_class = AvailableTimeSerializer
    queryset = AvailableTime.objects.all()
    permission_classes = (AllowAny,)
