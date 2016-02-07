from rest_framework import serializers
from common.models import ContactPointPeriod

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