from rest_framework import serializers
from common.models import DayOfWeek

class DayOfWeekSerializer(serializers.HyperlinkedModelSerializer):
    """
    Serializa un DayOfWeek
    """
    id = serializers.ReadOnlyField()

    def update(self, instance, validated_data):
        instance.value = validated_data['value']
        instance.save()
        return instance

    class Meta:
        model = DayOfWeek
        fields = ('id', 'value')