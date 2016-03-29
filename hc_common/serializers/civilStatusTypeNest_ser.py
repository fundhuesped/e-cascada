#!/usr/bin/python
# -*- coding: utf-8 -*-

from hc_common.models import CivilStatusType
from hc_common.serializers import TypeNestSerializer


class CivilStatusTypeNestSerializer(TypeNestSerializer):
    class Meta(TypeNestSerializer.Meta):
        model = CivilStatusType
