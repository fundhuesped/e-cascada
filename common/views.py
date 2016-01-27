from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny
from django.http import Http404
from common.models import Coding
from common.serializers import CodingSerializer

class CodingList(generics.ListCreateAPIView):
    """
    Crea un nuevo Coding, o lista los existentes.
    :param request: En caso de creacion, la representacion json del Coding.
    :return: En caso de GET, la representacion json de un Coding.
    """
    serializer_class = CodingSerializer
    queryset = Coding.objects.all()
    permission_classes = (AllowAny,)
    paginate_by = 100

    def get_queryset(self):
        """
        Filtrado opcional del query, en base a display o code
        """
        queryset = Coding.objects.all()
        display = self.request.query_params.get('display')
        code = self.request.query_params.get('code')

        if display is not None:
            queryset = queryset.filter(display=display)
        if code is not None:
            queryset = queryset.filter(code=code)
        return queryset


class CodingDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Devuelve, modifica o elimina una instancia de Coding
    :param request: En el caso de GET o DELETE, el pk del Coding como parte de la URL. En el caso de PUT, ademas, un objeto json representando el Coding
    :param pk: El primary key del Coding
    :return: En el caso de GET y PUT, una representacion de Coding
    """
    serializer_class = CodingSerializer
    queryset = Coding.objects.all()
    permission_classes = (AllowAny,)

    def get(self, request, *args, **kwargs):
        return generics.RetrieveUpdateDestroyAPIView.get(self, request, *args, **kwargs)
