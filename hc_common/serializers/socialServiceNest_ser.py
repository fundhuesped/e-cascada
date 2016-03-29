#!/usr/bin/python
# -*- coding: utf-8 -*-

from hc_common.models import SocialService
from hc_common.serializers import TypeNestSerializer


class SocialServiceNestSerializer(TypeNestSerializer):
    class Meta(TypeNestSerializer.Meta):
        model = SocialService
