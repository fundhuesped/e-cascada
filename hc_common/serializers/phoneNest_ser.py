#!/usr/bin/python
# -*- coding: utf-8 -*-

from rest_framework import serializers
from hc_common.models import Phone


class PhoneNestSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField()

    def create(self, validated_data):
        instance = Phone.objects.create(
            number=validated_data.get('number'),
            contact=validated_data.get('contact'),
            message=validated_data.get('message')
        )
        return instance

    def update(self, instance, validated_data):
        instance.number = validated_data.get('number', instance.number)
        instance.contact = validated_data.get('contact', instance.contact)
        instance.message = validated_data.get('message', instance.message)
        instance.save()

        return instance

    class Meta:
        model = Phone
        fields = ('id', 'number', 'contact', 'message')
