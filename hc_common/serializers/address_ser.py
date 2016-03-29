#!/usr/bin/python
# -*- coding: utf-8 -*-

from rest_framework import serializers
from hc_common.serializers import TypeSerializer
from hc_common.models import Address, Location


class AddressSerializer(TypeSerializer):
    location = serializers.HyperlinkedRelatedField(
        view_name="hc_common:Location-detail",
        queryset=Location.objects
    )

    class Meta(TypeSerializer.Meta):
        model = Address
        fields = ('id', 'name', 'description', 'status', 'location')
