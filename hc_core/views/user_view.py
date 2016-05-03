#!/usr/bin/python
# -*- coding: utf-8 -*-
from rest_framework import generics
from rest_framework.views import Response
from django.contrib.auth import login, logout
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import AllowAny
from hc_core.serializers import UserSerializer
from django.contrib.auth.models import User


class UserLogin(generics.CreateAPIView):
    serializer_class = UserSerializer
    def post(self, request, *args, **kwargs):
        login(request, request.user)
        return Response(UserSerializer(request.user).data)


class UserLogout(generics.DestroyAPIView):
    serializer_class = UserSerializer
    def delete(self, request, *args, **kwargs):
        logout(request)
        return Response({})
