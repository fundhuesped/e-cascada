from rest_framework import serializers
from practicioners.models import NotAvailablePeriod, NotAvailable

class NotAvailableSerializer(serializers.HyperlinkedModelSerializer):
    """
    Serializa un NotAvailable
    """
    id = serializers.ReadOnlyField()

    during = serializers.HyperlinkedRelatedField(
        view_name="practicioners:NotAvailablePeriod-detail",
        queryset=NotAvailablePeriod.objects
    )

    def update(self, instance, validated_data):
        instance.description = validated_data['description']
        instance.during = validated_data['during']
        return instance

    class Meta:
        model = NotAvailable
        fields = ('id', 'description', 'during')