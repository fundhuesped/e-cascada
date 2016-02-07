from rest_framework import serializers
from common.models import NamePeriod

class NamePeriodSerializer(serializers.Serializer):
    """
    Serializador de NamePeriod
    """
    id = serializers.ReadOnlyField()
    start = serializers.DateTimeField()
    end = serializers.DateTimeField()

    def create(self, validated_data):
        """
        Create an NamePeriod
        :param validated_data:
        :return:
        """
        return NamePeriod.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.start = validated_data.get('start', instance.start)
        instance.end = validated_data.get('end', instance.end)
        instance.save()
        return instance

    class Meta:
        model = NamePeriod
        fields = ('id', 'start', 'end')