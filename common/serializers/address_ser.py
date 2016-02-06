from rest_framework import serializers
from common.models import AddressPointPeriod, AddressLine

__author__ = 'Santi'

class AddressPointPeriodSerializer(serializers.Serializer):
    """
    Serializador de IdentifierPeriod
    """
    id = serializers.ReadOnlyField()
    start = serializers.DateTimeField()
    end = serializers.DateTimeField()

    def create(self, validated_data):
        """
        Create an IdentifierPeriod
        :param validated_data:
        :return:
        """
        return AddressPointPeriod.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.start = validated_data.get('start', instance.start)
        instance.end = validated_data.get('end', instance.end)
        instance.save()
        return instance

    class Meta:
        model = AddressPointPeriod
        fields = ('id', 'start', 'end')

class AddressLineSerializer(serializers.Serializer):
    """
    Serializa un AddressLine
    """
    id = serializers.ReadOnlyField()
    line = serializers.CharField()

    def create(self, validated_data):
        """
        Create an AddresLine
        :param validated_data:
        :return:
        """
        return AddressLine.objects.create(**validated_data)
    class Meta:
        model = AddressLine
        fields = ('id', 'line')

#TODO: Agregar serializer para Address