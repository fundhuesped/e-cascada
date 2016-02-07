from rest_framework import serializers
from common.models import NamePeriod, HumanName

class HumanNameSerializer(serializers.HyperlinkedModelSerializer):
    """
    Serializa un HumanName
    """
    id = serializers.ReadOnlyField()

    period = serializers.HyperlinkedRelatedField(
        view_name="common:NamePeriod-detail",
        queryset=NamePeriod.objects
    )

    def update(self, instance, validated_data):
        instance.use = validated_data['use']
        instance.text = validated_data['text']
        instance.family = validated_data['family']
        instance.given = validated_data['given']
        instance.prefix = validated_data['prefix']
        instance.suffix = validated_data['suffix']
        instance.period = validated_data['period']
        instance.save()
        return instance

    class Meta:
        model = HumanName
        fields = ('id', 'use', 'text', 'family', 'given', 'prefix', 'suffix', 'period')
