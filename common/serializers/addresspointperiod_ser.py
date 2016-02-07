from rest_framework import serializers
from common.models import AddressPointPeriod

class AddressPointPeriodSerializer(serializers.HyperlinkedModelSerializer):
    """
    Serializador de IdentifierPeriod
    """
    id = serializers.ReadOnlyField()
    start = serializers.DateTimeField()
    end = serializers.DateTimeField()

    def create(self, validated_data):
        """
        Create an AddressPointPeriod
        :param validated_data: Datos con los cuales crear la nueva instancia de AddressPointPeriod
        :return: La nueva instancia de AddressPointPeriod
        """
        return AddressPointPeriod.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Modifica un AddressPointPeriod
        :param instance: Instancia de AddressLinePeriod a modificar
        :param validated_data: Datos con los cuales modificar el AddressLinePeriod
        :return: Instancia modificada de AddressLinePeriod
        """
        instance.start = validated_data['start']
        instance.end = validated_data['end']
        instance.save()
        return instance

    class Meta:
        model = AddressPointPeriod
        fields = ('id', 'start', 'end')