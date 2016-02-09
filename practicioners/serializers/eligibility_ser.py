from rest_framework import serializers
from practicioners.models import Eligibility
from common.models import Coding

class EligibilitySerializer(serializers.HyperlinkedModelSerializer):
    """
    Serializa un Eligibility
    """
    id = serializers.ReadOnlyField()
    coding = serializers.HyperlinkedRelatedField(
        view_name="common:Coding-detail",
        queryset=Coding.objects,
    )
    def create(self, validated_data):
        """
        Crea un Eligibility
        :param validated_data: Valores con los cuales crear el Eligibility
        :return: Una nueva instancia de Eligibility
        """
        return Eligibility.objects.create(**validated_data)


    def update(self, instance, validated_data):
        """
        Modifica un Eligibility
        :param instance: Instancia de Eligibility a modificar
        :param validated_data: Nuevos valores con los que modificar Eligibility
        :return: Instancia de Eligibility modificada
        """
        instance.coding = validated_data['coding']
        instance.text = validated_data['text']
        instance.save()
        return instance

    class Meta:
        model = Eligibility
        fields = ('id', 'coding', 'text')