#!/usr/bin/python
# -*- coding: utf-8 -*-
from django.contrib.auth.models import User
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    password = serializers.Field(
        write_only=True
    )

    def validate(self, attrs):
        user = super(UserSerializer, self).validate(self, attrs)
        user.set_password(attrs['password'])
        return user

    class Meta:
        model = User
        fields = ('password', 'first_name', 'last_name', 'email',)
