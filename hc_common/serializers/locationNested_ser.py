#!/usr/bin/python
# -*- coding: utf-8 -*-

from rest_framework import serializers
from hc_common.serializers import TypeNestedSerializer
from hc_common.models import Location


class LocationNestedSerializer(TypeNestedSerializer):
    district = serializers.HyperlinkedIdentityField(
        view_name='hc_common:District-detail',
        lookup_field='pk'
    )

    class Meta(TypeNestedSerializer.Meta):
        model = Location
        fields = ('id', 'name', 'description', 'status', 'district')
