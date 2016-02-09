from rest_framework import serializers
from practicioners.models import ServiceProvisioningCode
from common.models import Coding

class ServiceProvisioningCodeSerializer(serializers.HyperlinkedModelSerializer):
    """
    Serializa un ServiceProvisioningCode
    """
    id = serializers.ReadOnlyField()
    coding = serializers.HyperlinkedRelatedField(
        view_name="common:Coding-detail",
        queryset=Coding.objects,
    )
    def create(self, validated_data):
        """
        Crea un ServiceProvisioningCode
        :param validated_data: Valores con los cuales crear el ServiceProvisioningCode
        :return: Una nueva instancia de ServiceProvisioningCode
        """
        return ServiceProvisioningCode.objects.create(**validated_data)


    def update(self, instance, validated_data):
        """
        Modifica un ServiceProvisioningCode
        :param instance: Instancia de ServiceProvisioningCode a modificar
        :param validated_data: Nuevos valores con los que modificar ServiceProvisioningCode
        :return: Instancia de ServiceProvisioningCode modificada
        """
        instance.coding = validated_data['coding']
        instance.text = validated_data['text']
        instance.save()
        return instance

    class Meta:
        model = ServiceProvisioningCode
        fields = ('id', 'coding', 'text')