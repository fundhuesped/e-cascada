#!/usr/bin/python
# -*- coding: utf-8 -*-

from rest_framework import serializers


class TypeSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.ReadOnlyField()

    def create(self, validated_data):
        return self.Meta.model.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data['name']
        instance.description = validated_data['description']
        instance.status = validated_data['status']
        instance.save()
        return instance

    class Meta:
        fields = ('id', 'name', 'description', 'status')
