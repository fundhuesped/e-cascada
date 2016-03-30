#!/usr/bin/python
# -*- coding: utf-8 -*-

from hc_common.serializers import TypeNestedSerializer
from hc_common.models import Province


class ProvinceNestedSerializer(TypeNestedSerializer):
    class Meta(TypeNestedSerializer.Meta):
        model = Province
