from rest_framework import serializers
from common.models import IdentifierType

class IdentifierTypeSerializer(serializers.HyperlinkedModelSerializer):
    """
    Serializador de un IdentifierType
    """
    id = serializers.IntegerField(read_only=True)
    coding = serializers.CharField(max_length=4)
    text = serializers.CharField()

    def create(self, validated_data):
        """
        Create the IdentifierType
        :param validated_data:
        :return:
        """
        return IdentifierType.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.coding = validated_data.get('coding', instance.coding)
        instance.text = validated_data.get('text', instance.text)
        instance.save()
        return instance

    class Meta:
        model = IdentifierType
        fields = ('id', 'coding', 'text')