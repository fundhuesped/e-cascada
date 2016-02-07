from rest_framework import serializers
from common.models import ContactPointPeriod, ContactPoint

class ContactPointSerializer(serializers.HyperlinkedModelSerializer):
    """
    Serializa un ContactPoint
    """
    id = serializers.ReadOnlyField()

    period = serializers.HyperlinkedRelatedField(
        view_name="common:ContactPointPeriod-detail",
        queryset=ContactPointPeriod.objects
    )

    def update(self, instance, validated_data):
        instance.system = validated_data['system']
        instance.value = validated_data['value']
        instance.use = validated_data['use']
        instance.rank = validated_data['rank']
        instance.period = validated_data['period']
        instance.save()
        return instance

    class Meta:
        model = ContactPoint
        fields = ('id', 'system', 'value', 'use', 'rank', 'period')
