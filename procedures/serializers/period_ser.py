from rest_framework import serializers
from procedures.models import Period
from common.models import Coding

class PeriodSerializer(serializers.HyperlinkedModelSerializer):
    """
    Serializa un Period
    """
    id = serializers.ReadOnlyField()
    coding = serializers.HyperlinkedRelatedField(
        view_name="common:Coding-detail",
        queryset=Coding.objects,
    )
    def create(self, validated_data):
        """
        Crea un Period
        :param validated_data: Valores con los cuales crear el Speciality
        :return: Una nueva instancia de Speciality
        """
        return Period.objects.create(**validated_data)


    def update(self, instance, validated_data):
        """
        Modifica un Period
        :param instance: Instancia de Speciality a modificar
        :param validated_data: Nuevos valores con los que modificar Speciality
        :return: Instancia de Speciality modificada
        """
        instance.coding = validated_data['coding']
        instance.text = validated_data['text']
        instance.save()
        return instance

    class Meta:
        model = Period
        fields = ('id', 'coding', 'text')