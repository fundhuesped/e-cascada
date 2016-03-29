#!/usr/bin/python
# -*- coding: utf-8 -*-

from rest_framework import serializers
from hc_common.models import Address
from hc_common.serializers import LocationNestSerializer


class AddressNestSerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField()

    location = LocationNestSerializer(
        many=False
    )

    def create(self, validated_data):
        location = validated_data.pop('location')
        address = Address.objects.create(
            name=validated_data.get('name'),
            description=validated_data.get('description'),
            status=validated_data.get('status'),
            location=location
        )
        return address

    def update(self, instance, validated_data):
        location = validated_data.pop('location')
        instance.name = validated_data.get('name', instance.name)
        instance.description = validated_data.get('description', instance.description)
        instance.status = validated_data.get('status', instance.status)
        instance.location = location
        instance.save()

        return instance

    class Meta:
        model = Address
        fields = ('id', 'status', 'name', 'description', 'location')
