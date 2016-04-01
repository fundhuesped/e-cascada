#!/usr/bin/python
# -*- coding: utf-8 -*-

from rest_framework import serializers
from hc_common.serializers import TypeSerializer
from hc_common.models import District, Location


class LocationSerializer(TypeSerializer):
    district = serializers.HyperlinkedRelatedField(
        view_name="hc_common:District-detail",
        queryset=District.objects
    )

    class Meta(TypeSerializer.Meta):
        model = Location
        fields = ('id', 'name', 'description', 'district')
