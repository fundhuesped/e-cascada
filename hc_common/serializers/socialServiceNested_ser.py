#!/usr/bin/python
# -*- coding: utf-8 -*-

from hc_common.models import SocialService
from hc_common.serializers import TypeNestedSerializer


class SocialServiceNestedSerializer(TypeNestedSerializer):
    class Meta(TypeNestedSerializer.Meta):
        model = SocialService
