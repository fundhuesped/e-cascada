#!/usr/bin/python
# -*- coding: utf-8 -*-

from hc_common.serializers import TypeSerializer
from hc_common.models import EducationType


class EducationTypeSerializer(TypeSerializer):
    class Meta(TypeSerializer.Meta):
        model = EducationType
