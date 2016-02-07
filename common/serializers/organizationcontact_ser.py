from rest_framework import serializers
from common.models import HumanName, ContactPoint, OrganizationContact, Address

class OrganizationContactSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.ReadOnlyField()
    name = serializers.HyperlinkedRelatedField(
        view_name="common:HumanName-detail",
        queryset=HumanName.objects
    )

    telecom = serializers.HyperlinkedRelatedField(
        view_name="common:ContactPoint-detail",
        queryset=ContactPoint.objects
    )

    address = serializers.HyperlinkedRelatedField(
        view_name="common:Address-detail",
        queryset=Address.objects
    )

    def update(self, instance, validated_data):
        instance.name = validated_data['name']
        instance.purpose = validated_data['purpose']
        instance.telecom = validated_data['telecom']
        instance.address = validated_data['address']
        instance.save()
        return instance
    
    class Meta:
        model = OrganizationContact
        fields = ('id', 'name', 'purpose', 'telecom', 'address')