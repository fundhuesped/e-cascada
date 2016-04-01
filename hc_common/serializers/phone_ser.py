#!/usr/bin/python
# -*- coding: utf-8 -*-

from rest_framework import serializers
from hc_common.models import Phone


class PhoneSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.ReadOnlyField()

    def create(self, validated_data):
        return self.Meta.model.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.number = validated_data['number']
        instance.contact = validated_data['contact']
        instance.message = validated_data['message']
        instance.save()
        return instance

    class Meta:
        model = Phone
        fields = ('id', 'number', 'contact', 'message')
