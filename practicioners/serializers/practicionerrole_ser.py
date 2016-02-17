from rest_framework import serializers
from practicioners.models import PracticionerRole, HealthcareService, PracticionerRolePeriod, Role, Speciality
from common.models import Organization, Location

class PracticionerRoleSerializer(serializers.HyperlinkedModelSerializer):
    """
    Serializa un PracticionerRole
    """
    id = serializers.ReadOnlyField()

    managingOrganization = serializers.HyperlinkedRelatedField(
        view_name="common:Organization-detail",
        queryset=Organization.objects
    )

    role = serializers.HyperlinkedRelatedField(
        view_name="practicioners:Role-detail",
        queryset=Role.objects
    )

    speciality = serializers.HyperlinkedRelatedField(
        view_name="practicioners:Speciality-detail",
        queryset=Speciality.objects,
        many=True
    )

    period = serializers.HyperlinkedRelatedField(
        view_name="practicioners:PracticionerRole-detail",
        queryset=PracticionerRolePeriod.objects
    )

    location = serializers.HyperlinkedRelatedField(
        view_name="common:Location-detail",
        queryset=Location.objects,
        many=True
    )

    healthCareService = serializers.HyperlinkedRelatedField(
        view_name="practicioners:HealthCareService-detail",
        queryset=HealthcareService.objects,
        many=True
    )

    def update(self, instance, validated_data):
        instance.managingOrganization = validated_data['managingOrganization']
        instance.role = validated_data['role']
        instance.speciality = validated_data['speciality']
        instance.period = validated_data['period']
        instance.location = validated_data['location']
        instance.healthCareService = validated_data['healthCareService']

        return instance

    class Meta:
        model = PracticionerRole
        fields = ('id', 'managingOrganization', 'role', 'speciality', 'period', 'location', 'healthCareService')