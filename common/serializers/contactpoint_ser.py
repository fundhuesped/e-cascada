from rest_framework import serializers
from common.models import ContactPointPeriod, ContactPoint

__author__ = 'Santi'

class ContactPointPeriodSerializer(serializers.HyperlinkedModelSerializer):
    """
    Serializador de IdentifierPeriod
    """
    id = serializers.ReadOnlyField()
    start = serializers.DateTimeField()
    end = serializers.DateTimeField()

    def update(self, instance, validated_data):
        instance.start = validated_data.get('start', instance.start)
        instance.end = validated_data.get('end', instance.end)
        instance.save()
        return instance

    class Meta:
        model = ContactPointPeriod
        fields = ('id','start', 'end')

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
