#!/usr/bin/python
# -*- coding: utf-8 -*-

from rest_framework import serializers
from hc_common.models import Phone


class PhoneNestedSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField()

    def to_internal_value(self, data):
        types = self.Meta.model.objects.filter(pk=data['id'])
        if types[0] is not None:
            return types[0]
        else:
            raise ValueError('Type not found')

    class Meta:
        model = Phone
        fields = ('id', 'number', 'contact', 'message')
