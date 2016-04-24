#!/usr/bin/python
# -*- coding: utf-8 -*-

from hc_common.serializers import TypeNestSerializer
from hc_common.models import DocumentType


class DocumentTypeSerializer(TypeNestSerializer):
    class Meta(TypeNestSerializer.Meta):
        model = DocumentType
