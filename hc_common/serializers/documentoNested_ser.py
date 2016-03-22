#!/usr/bin/python
# -*- coding: utf-8 -*-

from rest_framework import serializers
from hc_common.models import Documento

class DocumentoNestedSerializer(serializers.ModelSerializer):
    """
    Serializa un documento, para ser incluida como objeto nested en otro objeto
    """
    id = serializers.IntegerField()
    type = serializers.ReadOnlyField()
    number = serializers.ReadOnlyField()
    comments = serializers.ReadOnlyField()

    url = serializers.HyperlinkedIdentityField(
        view_name='hc_common:Documento-detail',
        lookup_field='pk'
    )

    def to_internal_value(self, data):
        documentos= Documento.objects.filter(pk=data['id'])
        if documentos[0] is not None:
            return documentos[0]
        else:
            raise ValueError('Documento not found')


    class Meta:
        model = Documento
        fields = ('id', 'type', 'number', 'comments', 'url')