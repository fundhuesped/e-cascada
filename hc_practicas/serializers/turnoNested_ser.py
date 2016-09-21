#!/usr/bin/python
# -*- coding: utf-8 -*-

from rest_framework import serializers
from hc_pacientes.models import Paciente
from hc_practicas.models import Turno
from hc_pacientes.serializers import PacienteNestedSerializer

class TurnoNestedSerializer(serializers.ModelSerializer):
    """
    Serializa un turno, para ser incluida como objeto nested en otro objeto
    """

    id = serializers.IntegerField()
    state=serializers.ReadOnlyField()
    status=serializers.ReadOnlyField()
    notes=serializers.ReadOnlyField()
    paciente= PacienteNestedSerializer(
        many=False,
        read_only=True
    )

    url = serializers.HyperlinkedIdentityField(
        view_name='api:hc_practicas:Turno-detail',
        lookup_field='pk'
    )


    def to_internal_value(self, data):
        if (isinstance(data, list) or isinstance(data, dict)):
            turnos= Turno.objects.filter(pk=data['id'])
        else:
            turnos=Turno.objects.filter(pk=data)

        if turnos.count()>0:
            return turnos[0]
        else:
            raise ValueError('Turno not found')


    class Meta:
        model = Turno
        fields = ('id', 'paciente', 'state', 'status', 'notes', 'url')
