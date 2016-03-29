#!/usr/bin/python
# -*- coding: utf-8 -*-

from hc_common.models import EducationType
from hc_common.serializers import TypeNestSerializer


class EducationTypeNestSerializer(TypeNestSerializer):
    class Meta(TypeNestSerializer.Meta):
        model = EducationType
