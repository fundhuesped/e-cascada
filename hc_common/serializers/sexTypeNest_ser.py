#!/usr/bin/python
# -*- coding: utf-8 -*-

from hc_common.models import SexType
from hc_common.serializers import TypeNestSerializer


class SexTypeNestSerializer(TypeNestSerializer):
    class Meta:
        model = SexType
