#!/usr/bin/python
# -*- coding: utf-8 -*-


from rest_framework import serializers
from hc_practicas.models import ProfesionalMeta

class ProfesionalMetaNestedSerializer(serializers.ModelSerializer):
    """
    Serializa un Meta Profesional, para ser incluida como objeto nested en otro objeto
    """
    id = serializers.IntegerField()
    metaType = serializers.ReadOnlyField()
    metaValue = serializers.ReadOnlyField()

    url = serializers.HyperlinkedIdentityField(
        view_name='hc_practicas:ProfesionalMeta-detail',
        lookup_field='pk'
    )

    def to_internal_value(self, data):
        profesionalMetas= ProfesionalMeta.objects.filter(pk=data['id'])
        if profesionalMetas[0] is not None:
            return profesionalMetas[0]
        else:
            raise ValueError('Meta Profesional not found')


    class Meta:
        model = ProfesionalMeta
        fields = ('id', 'metaType', 'metaValue','url')