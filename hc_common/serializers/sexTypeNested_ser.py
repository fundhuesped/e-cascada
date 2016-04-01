#!/usr/bin/python
# -*- coding: utf-8 -*-

from hc_common.models import SexType
from hc_common.serializers import TypeNestedSerializer


class SexTypeNestedSerializer(TypeNestedSerializer):
    class Meta(TypeNestedSerializer.Meta):
        model = SexType