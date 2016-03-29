#!/usr/bin/python
# -*- coding: utf-8 -*-

from hc_common.models import DocumentType
from hc_common.serializers import TypeNestSerializer


class DocumentTypeNestSerializer(TypeNestSerializer):
    class Meta(TypeNestSerializer.Meta):
        model = DocumentType
