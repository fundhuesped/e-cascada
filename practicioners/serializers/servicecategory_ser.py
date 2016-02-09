from rest_framework import serializers
from practicioners.models import ServiceCategory
from common.models import Coding

class ServiceCategorySerializer(serializers.HyperlinkedModelSerializer):
    """
    Serializa un ServiceCategory
    """
    id = serializers.ReadOnlyField()
    coding = serializers.HyperlinkedRelatedField(
        view_name="common:Coding-detail",
        queryset=Coding.objects,
    )
    def create(self, validated_data):
        """
        Crea un ServiceCategory
        :param validated_data: Valores con los cuales crear el ServiceCategory
        :return: Una nueva instancia de ServiceCategory
        """
        return ServiceCategory.objects.create(**validated_data)


    def update(self, instance, validated_data):
        """
        Modifica un ServiceCategory
        :param instance: Instancia de ServiceCategory a modificar
        :param validated_data: Nuevos valores con los que modificar ServiceCategory
        :return: Instancia de ServiceCategory modificada
        """
        instance.coding = validated_data['coding']
        instance.text = validated_data['text']
        instance.save()
        return instance

    class Meta:
        model = ServiceCategory
        fields = ('id', 'coding', 'text')