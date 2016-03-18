from rest_framework import serializers
from practicioners.models import PracticionerRolePeriod

class PracticionerRolePeriodSerializer(serializers.HyperlinkedModelSerializer):
    """
    Serializador de PracticionerRole
    """
    id = serializers.ReadOnlyField()
    start = serializers.DateTimeField()
    end = serializers.DateTimeField()

    def create(self, validated_data):
        """
        Create an PracticionerRolePeriod
        :param validated_data: Datos con los cuales crear la nueva instancia de PracticionerRolePeriod
        :return: La nueva instancia de PracticionerRolePeriod
        """
        return PracticionerRolePeriod.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Modifica un PracticionerRolePeriod
        :param instance: Instancia de PracticionerRolePeriod a modificar
        :param validated_data: Datos con los cuales modificar el PracticionerRolePeriod
        :return: Instancia modificada de PracticionerRolePeriod
        """
        instance.start = validated_data['start']
        instance.end = validated_data['end']
        instance.save()
        return instance

    class Meta:
        model = PracticionerRolePeriod
        fields = ('id', 'start', 'end')