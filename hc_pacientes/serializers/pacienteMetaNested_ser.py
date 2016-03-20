#!/usr/bin/python
# -*- coding: utf-8 -*-


from rest_framework import serializers
from hc_pacientes.models import PacienteMeta

class PacienteMetaNestedSerializer(serializers.ModelSerializer):
    """
    Serializa un MetaPaciente, para ser incluida como objeto nested en otro objeto
    """
    id = serializers.IntegerField()
    metaType = serializers.ReadOnlyField()
    metaValue = serializers.ReadOnlyField()

    url = serializers.HyperlinkedIdentityField(
        view_name='hc_pacientes:PacienteMeta-detail',
        lookup_field='pk'
    )

    def to_internal_value(self, data):
        pacienteMetas= PacienteMeta.objects.filter(pk=data['id'])
        if pacienteMetas[0] is not None:
            return pacienteMetas[0]
        else:
            raise ValueError('Meta Paciente not found')


    class Meta:
        model = PacienteMeta
        fields = ('id', 'metaType', 'metaValue','url')