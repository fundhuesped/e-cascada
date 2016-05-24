#!/usr/bin/python
# -*- coding: utf-8 -*-
from rest_framework import generics
from rest_framework.views import Response
from django.contrib.auth import login, logout
from rest_framework.permissions import AllowAny
from hc_core.serializers import UserSerializer
from rest_framework.authtoken.models import Token


class UserLogin(generics.CreateAPIView):
    serializer_class = UserSerializer
    permission_classes = AllowAny,
    def post(self, request, *args, **kwargs):
        login(request, request.user)
        tokens = Token.objects.filter(user=request.user)
        if tokens.count()>=1:
            token = tokens[0]
        else:
            token = Token.objects.create(user=request.user)
        return Response(UserSerializer(request.user).data, headers={'auth-token': token.key})


class UserLogout(generics.DestroyAPIView):
    serializer_class = UserSerializer
    permission_classes = AllowAny,
    def delete(self, request, *args, **kwargs):
        logout(request)
        return Response({})
