#!/usr/bin/python
# -*- coding: utf-8 -*-

from hc_common.serializers import TypeSerializer
from hc_common.models import DocumentType


class DocumentTypeSerializer(TypeSerializer):
    class Meta(TypeSerializer.Meta):
        model = DocumentType