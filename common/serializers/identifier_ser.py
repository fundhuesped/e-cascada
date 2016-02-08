from rest_framework import serializers
from common.models import IdentifierPeriod, IdentifierType, Identifier

class IdentifierSerializer(serializers.HyperlinkedModelSerializer):
    """
    Serializador para Identifier
    """

    id = serializers.ReadOnlyField()
    type = serializers.HyperlinkedRelatedField(
        view_name="common:IdentifierType-detail",
        queryset=IdentifierType.objects
    )
    period = serializers.HyperlinkedRelatedField(
        view_name="common:IdentifierPeriod-detail",
        queryset=IdentifierPeriod.objects
    )

    def create(self, validated_data):
        """
        Crea un Identifier
        :param validated_data:
        :return:
        """
        return Identifier(**validated_data)

    def update(self, instance, validated_data):
        """
        Modifica un identifier
        :param instance:
        :param validated_data:
        :return:
        """
        instance.use = validated_data['use']
        instance.type = validated_data['type']
        instance.system = validated_data['system']
        instance.value = validated_data['value']
        instance.period = validated_data['period']
        instance.assigner = validated_data['assigner']
        instance.save()
        return instance


    class Meta:
        model = Identifier
        fields = ('id', 'use', 'type', 'system', 'value', 'period', 'assigner')