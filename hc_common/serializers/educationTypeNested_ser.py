#!/usr/bin/python
# -*- coding: utf-8 -*-

from hc_common.models import EducationType
from hc_common.serializers import TypeNestedSerializer


class EducationTypeNestedSerializer(TypeNestedSerializer):
    class Meta(TypeNestedSerializer.Meta):
        model = EducationType
