#!/usr/bin/python
# -*- coding: utf-8 -*-

from rest_framework import serializers
from hc_common.models import Location


class LocationNestedSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField()
    name = serializers.ReadOnlyField()
    description = serializers.ReadOnlyField()
    status = serializers.ReadOnlyField()

    district = serializers.HyperlinkedIdentityField(
        view_name='hc_common:District-detail',
        lookup_field='pk'
    )

    def to_internal_value(self, data):
        types = self.Meta.model.objects.filter(pk=data['id'])
        if types[0] is not None:
            return types[0]
        else:
            raise ValueError('Type not found')

    class Meta:
        model = Location
        fields = ('id', 'name', 'description', 'status', 'district')
