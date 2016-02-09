from rest_framework import serializers
from practicioners.models import Speciality
from common.models import Coding

class SpecialitySerializer(serializers.HyperlinkedModelSerializer):
    """
    Serializa un Speciality
    """
    id = serializers.ReadOnlyField()
    coding = serializers.HyperlinkedRelatedField(
        view_name="common:Coding-detail",
        queryset=Coding.objects,
    )
    def create(self, validated_data):
        """
        Crea un Speciality
        :param validated_data: Valores con los cuales crear el Speciality
        :return: Una nueva instancia de Speciality
        """
        return Speciality.objects.create(**validated_data)


    def update(self, instance, validated_data):
        """
        Modifica un Speciality
        :param instance: Instancia de Speciality a modificar
        :param validated_data: Nuevos valores con los que modificar Speciality
        :return: Instancia de Speciality modificada
        """
        instance.coding = validated_data['coding']
        instance.text = validated_data['text']
        instance.save()
        return instance

    class Meta:
        model = Speciality
        fields = ('id', 'coding', 'text')