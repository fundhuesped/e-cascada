from rest_framework import serializers
from common.models import NamePeriod

class NamePeriodSerializer(serializers.Serializer):
    """
    Serializador de NamePeriod
    """
    id = serializers.ReadOnlyField()
    start = serializers.DateTimeField()
    end = serializers.DateTimeField()

    def create(self, validated_data):
        """
        Create an NamePeriod
        :param validated_data:
        :return:
        """
        return NamePeriod.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.start = validated_data.get('start', instance.start)
        instance.end = validated_data.get('end', instance.end)
        instance.save()
        return instance

    def update(self, instance, validated_data):
        """
        Modifica y devuelve una instancia de AddressLine
        :param instance:
        :param validated_data: Datos validos para crear AddressLine
        :return: Instancia de AddressLine
        """
        instance.line = validated_data.get('line', instance.line)
        instance.save()
        return instance
    class Meta:
        model = NamePeriod
        fields = ('id', 'start', 'end')

#TODO: Agregar serializer para HumanName
