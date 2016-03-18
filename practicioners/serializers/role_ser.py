from rest_framework import serializers
from practicioners.models import Role
from common.models import Coding

class RoleSerializer(serializers.HyperlinkedModelSerializer):
    """
    Serializa un Role
    """
    id = serializers.ReadOnlyField()
    coding = serializers.HyperlinkedRelatedField(
        view_name="common:Coding-detail",
        queryset=Coding.objects,
    )
    def create(self, validated_data):
        """
        Crea un Role
        :param validated_data: Valores con los cuales crear el Role
        :return: Una nueva instancia de Role
        """
        return Role.objects.create(**validated_data)


    def update(self, instance, validated_data):
        """
        Modifica un Role
        :param instance: Instancia de Role a modificar
        :param validated_data: Nuevos valores con los que modificar Role
        :return: Instancia de Role modificada
        """
        instance.coding = validated_data['coding']
        instance.text = validated_data['text']
        instance.save()
        return instance

    class Meta:
        model = Role
        fields = ('id', 'coding', 'text')