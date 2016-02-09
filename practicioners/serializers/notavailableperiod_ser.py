from rest_framework import serializers
from practicioners.models import NotAvailablePeriod

class NotAvailablePeriodSerializer(serializers.HyperlinkedModelSerializer):
    """
    Serializador de NotAvailablePeriod
    """
    id = serializers.ReadOnlyField()
    start = serializers.DateTimeField()
    end = serializers.DateTimeField()

    def create(self, validated_data):
        """
        Create an NotAvailablePeriod
        :param validated_data: Datos con los cuales crear la nueva instancia de NotAvailablePeriod
        :return: La nueva instancia de NotAvailablePeriod
        """
        return NotAvailablePeriod.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Modifica un NotAvailablePeriod
        :param instance: Instancia de NotAvailablePeriod a modificar
        :param validated_data: Datos con los cuales modificar el NotAvailablePeriod
        :return: Instancia modificada de NotAvailablePeriod
        """
        instance.start = validated_data['start']
        instance.end = validated_data['end']
        instance.save()
        return instance

    class Meta:
        model = NotAvailablePeriod
        fields = ('id', 'start', 'end')