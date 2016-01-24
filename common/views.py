from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404
from common.models import Coding
from common.serializers import CodingSerializer

class CodingList(APIView):
    """
    Crea un nuevo Coding, o lista los existentes.
    :param request: En caso de creacion, la representacion json del Coding.
    :return: En caso de GET, la representacion json de un Coding.
    """
    def get(self, request):
        codings = Coding.objects.all()
        serializer = CodingSerializer(codings,many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = CodingSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

"""
@api_view(['GET', 'POST'])
def coding_list(request):
    if request.method == 'GET':
        codings = Coding.objects.all()
        serializer = CodingSerializer(codings,many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = CodingSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
"""
class CodingDetail(APIView):
    """
    Devuelve, modifica o elimina una instancia de Coding
    :param request: En el caso de GET o DELETE, el pk del Coding como parte de la URL. En el caso de PUT, ademas, un objeto json representando el Coding
    :param pk: El primary key del Coding
    :return: En el caso de GET y PUT, una representacion de Coding
    """
    def get_object(self, pk):
        try:
            return Coding.objects.get(pk=pk)
        except Coding.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        coding = self.get_object(pk)
        serializer = CodingSerializer(coding)
        return Response(serializer.data)

    def put(self, request, pk):
        coding = self.get(pk)
        serializer = CodingSerializer(coding, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        coding = self.get_object(pk)
        coding.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

"""
@api_view(['GET', 'PUT', 'DELETE'])
def coding_detail(request, pk):

    try:
        coding = Coding.objects.get(pk=pk)
    except Coding.DoesNotExist:
        return HttpResponse(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = CodingSerializer(coding)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = CodingSerializer(coding, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        coding.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
"""
