#!/usr/bin/python
# -*- coding: utf-8 -*-

from hc_common.models import DocumentType
from hc_common.serializers import TypeNestedSerializer


class DocumentTypeNestedSerializer(TypeNestedSerializer):

    class Meta(TypeNestedSerializer.Meta):
        model = DocumentType
