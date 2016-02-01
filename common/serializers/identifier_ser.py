from rest_framework import serializers
from common.models import IdentifierPeriod, IdentifierType

class IdentifierTypeSerializer(serializers.Serializer):
    """
    Serializador de un IdentifierType
    """
    pk = serializers.IntegerField(read_only=True)
    coding = serializers.CharField(max_length=4)
    text = serializers.CharField()

    def create(self, validated_data):
        """
        Create the IdentifierType
        :param validated_data:
        :return:
        """
        return IdentifierType.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.coding = validated_data.get('coding', instance.coding)
        instance.text = validated_data.get('text', instance.text)
        instance.save()
        return instance

class IdentifierPeriodSerializer(serializers.Serializer):
    """
    Serializador de IdentifierPeriod
    """
    start = serializers.DateTimeField()
    end = serializers.DateTimeField()

    def create(self, validated_data):
        """
        Create an IdentifierPeriod
        :param validated_data:
        :return:
        """
        return IdentifierPeriod.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.start = validated_data.get('start', instance.start)
        instance.end = validated_data.get('end', instance.end)
        instance.save()
        return instance

#TODO: Agregar serializaer para Identifier