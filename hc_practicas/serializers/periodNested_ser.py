#!/usr/bin/python
# -*- coding: utf-8 -*-

from rest_framework import serializers
from hc_practicas.models import Period
from hc_practicas.serializers import DayOfWeekNestedSerializer

class PeriodNestedSerializer(serializers.ModelSerializer):
    """
    Serializa un Periodo, para ser incluida como objeto nested en otro objeto
    """

    id = serializers.IntegerField()
    start = serializers.ReadOnlyField()
    end = serializers.ReadOnlyField()
    selected = serializers.ReadOnlyField()
    daysOfWeek = DayOfWeekNestedSerializer(
        many=True
    )

    url = serializers.HyperlinkedIdentityField(
        view_name='hc_practicas:Periodo-detail',
        lookup_field='pk'
    )

    def to_internal_value(self, data):
        periodos= Period.objects.filter(pk=data['id'])
        if periodos.count()>0:
            return periodos[0]
        else:
            raise ValueError('Periodo not found')


    class Meta:
        model = Period
        fields = ('id', 'start', 'end', 'selected', 'daysOfWeek')