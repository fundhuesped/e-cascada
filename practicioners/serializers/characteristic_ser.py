from rest_framework import serializers
from practicioners.models import Characteristic
from common.models import Coding

class CharacteristicSerializer(serializers.HyperlinkedModelSerializer):
    """
    Serializa un Characteristic
    """
    id = serializers.ReadOnlyField()
    coding = serializers.HyperlinkedRelatedField(
        view_name="common:Coding-detail",
        queryset=Coding.objects,
    )
    def create(self, validated_data):
        """
        Crea un Characteristic
        :param validated_data: Valores con los cuales crear el Characteristic
        :return: Una nueva instancia de Characteristic
        """
        return Characteristic.objects.create(**validated_data)


    def update(self, instance, validated_data):
        """
        Modifica un Characteristic
        :param instance: Instancia de Characteristic a modificar
        :param validated_data: Nuevos valores con los que modificar Characteristic
        :return: Instancia de Characteristic modificada
        """
        instance.coding = validated_data['coding']
        instance.text = validated_data['text']
        instance.save()
        return instance

    class Meta:
        model = Characteristic
        fields = ('id', 'coding', 'text')