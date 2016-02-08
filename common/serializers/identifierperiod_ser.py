from rest_framework import serializers
from common.models import IdentifierPeriod

class IdentifierPeriodSerializer(serializers.HyperlinkedModelSerializer):
    """
    Serializador de IdentifierPeriod
    """
    id = serializers.ReadOnlyField()
    start = serializers.DateTimeField()
    end = serializers.DateTimeField()

    def create(self, validated_data):
        """
        Create an IdentifierPeriod
        :param validated_data:
        :return:
        """
        return IdentifierPeriod.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.start = validated_data.get('start', instance.start)
        instance.end = validated_data.get('end', instance.end)
        instance.save()
        return instance

    class Meta:
        model = IdentifierPeriod
        fields = ('id', 'start', 'end')