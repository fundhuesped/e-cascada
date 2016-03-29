#!/usr/bin/python
# -*- coding: utf-8 -*-

from rest_framework import serializers
from hc_common.models import Phone
from hc_common.serializers import PhoneTypeNestSerializer


class PhoneNestSerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField()

    type = PhoneTypeNestSerializer(
        many=False
    )

    def create(self, validated_data):
        type = validated_data.pop('type')
        phone = Phone.objects.create(
            number=validated_data.get('number'),
            contact=validated_data.get('contact'),
            message=validated_data.get('message'),
            type=type
        )
        return phone

    def update(self, instance, validated_data):
        type = validated_data.pop('type')
        instance.number = validated_data.get('number', instance.number)
        instance.contact = validated_data.get('contact', instance.contact)
        instance.message = validated_data.get('message', instance.message)
        instance.type = type
        instance.save()

        return instance

    class Meta:
        model = Phone
        fields = ('id', 'type', 'number', 'contact', 'message')
