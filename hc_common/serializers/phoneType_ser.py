#!/usr/bin/python
# -*- coding: utf-8 -*-

from hc_common.serializers import TypeSerializer
from hc_common.models import PhoneType


class PhoneTypeSerializer(TypeSerializer):
    class Meta(TypeSerializer.Meta):
        model = PhoneType
