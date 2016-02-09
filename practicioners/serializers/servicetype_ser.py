from rest_framework import serializers
from practicioners.models import TypeService, Speciality, ServiceType

class ServiceTypeSerializer(serializers.HyperlinkedModelSerializer):
    """
    Serializa un NotAvailable
    """
    id = serializers.ReadOnlyField()

    type = serializers.HyperlinkedRelatedField(
        view_name="practicioners:TypeService-detail",
        queryset=TypeService.objects
    )

    speciality = serializers.HyperlinkedRelatedField(
        view_name="practicioners:Speciality-detail",
        queryset=Speciality.objects
    )

    def update(self, instance, validated_data):
        instance.type = validated_data['type']
        instance.speciality = validated_data['speciality']
        return instance

    class Meta:
        model = ServiceType
        fields = ('id', 'type', 'speciality')