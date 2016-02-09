from rest_framework import serializers
from practicioners.models import TypeService
from common.models import Coding

class TypeServiceSerializer(serializers.HyperlinkedModelSerializer):
    """
    Serializa un TypeService
    """
    id = serializers.ReadOnlyField()
    coding = serializers.HyperlinkedRelatedField(
        view_name="common:Coding-detail",
        queryset=Coding.objects,
    )
    def create(self, validated_data):
        """
        Crea un TypeService
        :param validated_data: Valores con los cuales crear el TypeService
        :return: Una nueva instancia de TypeService
        """
        return TypeService.objects.create(**validated_data)


    def update(self, instance, validated_data):
        """
        Modifica un TypeService
        :param instance: Instancia de TypeService a modificar
        :param validated_data: Nuevos valores con los que modificar TypeService
        :return: Instancia de TypeService modificada
        """
        instance.coding = validated_data['coding']
        instance.text = validated_data['text']
        instance.save()
        return instance

    class Meta:
        model = TypeService
        fields = ('id', 'coding', 'text')