#!/usr/bin/python
# -*- coding: utf-8 -*-

from hc_common.models import Province
from hc_common.serializers import TypeNestSerializer


class ProvinceNestSerializer(TypeNestSerializer):
    class Meta:
        model = Province
