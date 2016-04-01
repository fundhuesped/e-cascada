#!/usr/bin/python
# -*- coding: utf-8 -*-

from rest_framework import serializers
from hc_common.serializers import TypeNestedSerializer
from hc_common.models import District


class DistrictNestedSerializer(TypeNestedSerializer):
    province = serializers.HyperlinkedIdentityField(
        view_name='hc_common:Province-detail',
        lookup_field='pk'
    )

    class Meta(TypeNestedSerializer.Meta):
        model = District
        fields = ('id', 'name', 'description', 'status', 'province')
