#!/usr/bin/python
# -*- coding: utf-8 -*-

from rest_framework import serializers
from hc_common.serializers import TypeSerializer
from hc_common.models import District, Province


class DistrictSerializer(TypeSerializer):
    province = serializers.HyperlinkedRelatedField(
        view_name="hc_common:Province-detail",
        queryset=Province.objects
    )

    class Meta(TypeSerializer.Meta):
        model = District
        fields = ('id', 'name', 'description', 'province')
