#!/usr/bin/python
# -*- coding: utf-8 -*-

from hc_common.models import CivilStatusType
from hc_common.serializers import TypeNestedSerializer


class CivilStatusTypeNestedSerializer(TypeNestedSerializer):
    class Meta(TypeNestedSerializer.Meta):
        model = CivilStatusType
