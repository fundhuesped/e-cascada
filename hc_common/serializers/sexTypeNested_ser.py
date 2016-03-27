#!/usr/bin/python
# -*- coding: utf-8 -*-

from rest_framework import serializers
from hc_common.models import SexType

class SexTypeNestedSerializer(serializers.ModelSerializer):
    """
    Serializa un Tipo de sexo, para ser incluida como objeto nested en otro objeto
    """
    id = serializers.IntegerField()
    name = serializers.ReadOnlyField()
    description = serializers.ReadOnlyField()
    status = serializers.ReadOnlyField()

    url = serializers.HyperlinkedIdentityField(
        view_name='hc_common:SexType-detail',
        lookup_field='pk'
    )

    def to_internal_value(self, data):
        types = SexType.objects.filter(pk=data['id'])
        if types[0] is not None:
            return types[0]
        else:
            raise ValueError('Sex Type not found')

    class Meta:
        model = SexType
        fields = ('id', 'name', 'description', 'status', 'url')