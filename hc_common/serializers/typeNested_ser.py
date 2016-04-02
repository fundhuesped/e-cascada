#!/usr/bin/python
# -*- coding: utf-8 -*-

from rest_framework import serializers


class TypeNestedSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField()
    name = serializers.ReadOnlyField()
    description = serializers.ReadOnlyField()
    status = serializers.ReadOnlyField()

    def to_internal_value(self, data):
        types = self.Meta.model.objects.filter(pk=data['id'])
        if types:
            return types[0]
        else:
            raise ValueError('Type not found')

    class Meta:
        fields = ('id', 'name', 'description', 'status')
