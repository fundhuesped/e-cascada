#!/usr/bin/python
# -*- coding: utf-8 -*-

from rest_framework import serializers
from hc_common.models import DocumentType

class DocumentTypeNestedSerializer(serializers.ModelSerializer):
    """
    Serializa un Tipo de documento, para ser incluida como objeto nested en otro objeto
    """
    id = serializers.IntegerField()
    name = serializers.ReadOnlyField()
    description = serializers.ReadOnlyField()
    status = serializers.ReadOnlyField()

    url = serializers.HyperlinkedIdentityField(
        view_name='hc_common:DocumentType-detail',
        lookup_field='pk'
    )

    def to_internal_value(self, data):
        documents = DocumentType.objects.filter(pk=data['id'])
        if documents[0] is not None:
            return documents[0]
        else:
            raise ValueError('Tipo documento not found')

    class Meta:
        model = DocumentType
        fields = ('id', 'name', 'description', 'status', 'url')