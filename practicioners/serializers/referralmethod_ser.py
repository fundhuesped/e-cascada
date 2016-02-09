from rest_framework import serializers
from practicioners.models import ReferralMethod
from common.models import Coding

class ReferralMethodSerializer(serializers.HyperlinkedModelSerializer):
    """
    Serializa un ReferralMethod
    """
    id = serializers.ReadOnlyField()
    coding = serializers.HyperlinkedRelatedField(
        view_name="common:Coding-detail",
        queryset=Coding.objects,
    )
    def create(self, validated_data):
        """
        Crea un ReferralMethod
        :param validated_data: Valores con los cuales crear el ReferralMethod
        :return: Una nueva instancia de ReferralMethod
        """
        return ReferralMethod.objects.create(**validated_data)


    def update(self, instance, validated_data):
        """
        Modifica un ReferralMethod
        :param instance: Instancia de ReferralMethod a modificar
        :param validated_data: Nuevos valores con los que modificar ReferralMethod
        :return: Instancia de ReferralMethod modificada
        """
        instance.coding = validated_data['coding']
        instance.text = validated_data['text']
        instance.save()
        return instance

    class Meta:
        model = ReferralMethod
        fields = ('id', 'coding', 'text')