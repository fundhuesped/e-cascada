#!/usr/bin/python
# -*- coding: utf-8 -*-

from hc_common.serializers import TypeSerializer
from hc_common.models import SocialService


class SocialServiceSerializer(TypeSerializer):
    class Meta(TypeSerializer.Meta):
        model = SocialService
