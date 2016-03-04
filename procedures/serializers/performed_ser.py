from rest_framework import serializers
from procedures.models import ProcedurePeriod, Performed

class PerformedSerializer(serializers.HyperlinkedModelSerializer):
    """
    Serializa un Performed
    """
    id = serializers.ReadOnlyField()

    performedPeriod = serializers.HyperlinkedRelatedField(
        view_name="procedures:ProcedurePeriod-detail",
        queryset=ProcedurePeriod.objects
    )

    def create(self, validated_data):
        return Performed.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.performedDateTime = validated_data['performedDateTime']
        instance.performedPeriod = validated_data['performedPeriod']
        instance.save()
        return instance

    class Meta:
        model = Performed
        fields = ('id', 'performedDateTime', 'performedPeriod')
