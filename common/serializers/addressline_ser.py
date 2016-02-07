from rest_framework import serializers
from common.models import AddressLine

class AddressLineSerializer(serializers.HyperlinkedModelSerializer):
    """
    Serializa un AddressLine
    """
    id = serializers.ReadOnlyField()
    line = serializers.CharField()

    def create(self, validated_data):
        """
        Create an AddresLine
        :param validated_data: Datos con los cuales crear el AddressLine
        :return: Instancia de AddressLine creada
        """
        return AddressLine.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Modifica la instancia de AddressLine
        :param instance: Instancia de AddressLine a modificar
        :param validated_data: Datos con los cuales modificar a AddressLine
        :return: La instancia modificada de AddressLine
        """
        instance.line = validated_data['line']
        instance.save()
        return instance

    class Meta:
        model = AddressLine
        fields = ('id', 'line')