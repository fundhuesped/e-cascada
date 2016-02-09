from rest_framework import serializers
from practicioners.models import HealthcareService, ServiceCategory, ServiceType, ServiceProvisioningCode, Eligibility, Characteristic, ReferralMethod, AvailableTime, NotAvailable
from common.models import Identifier, Organization, ContactPoint

class HealthCareServiceSerializer(serializers.HyperlinkedModelSerializer):
    """
    Serializa un HealthCareService
    """
    id = serializers.ReadOnlyField()

    identifier = serializers.HyperlinkedRelatedField(
        view_name="common:Identifier-detail",
        queryset=Identifier.objects,
        many=True
    )

    providedBy = serializers.HyperlinkedRelatedField(
        view_name="common:Organization-detail",
        queryset=Organization.objects
    )

    serviceCategory = serializers.HyperlinkedRelatedField(
        view_name="practicioners:ServiceCategory-detail",
        queryset=ServiceCategory.objects
    )

    serviceType = serializers.HyperlinkedRelatedField(
        view_name="practicioners:ServiceType-detail",
        queryset=ServiceType.objects,
        many=True
    )

    telecom = serializers.HyperlinkedRelatedField(
        view_name="common:ContactPoint-detail",
        queryset=ContactPoint.objects,
        many=True
    )

    serviceProvisioningCode = serializers.HyperlinkedRelatedField(
        view_name="practicioners:ServiceProvisioningCode-detail",
        queryset=ServiceProvisioningCode.objects,
        many=True
    )

    eligibility = serializers.HyperlinkedRelatedField(
        view_name="practicioners:Eligibility-detail",
        queryset=Eligibility.objects
    )

    characteristic = serializers.HyperlinkedRelatedField(
        view_name="practicioners:Characteristic-detail",
        queryset=Characteristic.objects,
        many=True
    )

    referralMethod = serializers.HyperlinkedRelatedField(
        view_name="practicioners:ReferralMethod-detail",
        queryset=ReferralMethod.objects,
        many=True
    )

    availableTime = serializers.HyperlinkedRelatedField(
        view_name="practicioners:AvailableTime-detail",
        queryset=AvailableTime.objects,
        many=True
    )

    notAvailable = serializers.HyperlinkedRelatedField(
        view_name="practicioners:NotAvailable-detail",
        queryset=NotAvailable.objects,
        many=True
    )

    def update(self, instance, validated_data):
        instance.identifier = validated_data['identifier']
        instance.providedBy = validated_data['providedBy']
        instance.serviceCategory = validated_data['serviceCategory']
        instance.serviceType = validated_data['serviceType']
        instance.location = validated_data['location']
        instance.serviceName = validated_data['serviceName']
        instance.comment = validated_data['comment']
        instance.extraDetails = validated_data['extraDetails']
        instance.photo = validated_data['photo']
        instance.telecom = validated_data['telecom']
        instance.coverageArea = validated_data['coverageArea']
        instance.serviceProvisioningCode = validated_data['serviceProvisioningCode']
        instance.eligibility = validated_data['eligibility']
        instance.eligibilityNote = validated_data['eligibilityNote']
        instance.programName = validated_data['programName']
        instance.characteristic = validated_data['characteristic']
        instance.referralMethod = validated_data['referralMethod']
        instance.publicKey = validated_data['publicKey']
        instance.appointmentRequired = validated_data['appointmentRequired']
        instance.availableTime = validated_data['availableTime']
        instance.notAvailable = validated_data['notAvailable']
        instance.availabilityExceptions = validated_data['availabilityExceptions']
        return instance

    class Meta:
        model = HealthcareService
        fields = ('id', 'identifier', 'providedBy', 'serviceCategory', 'serviceType', 'location', 'serviceName', 'comment', 'extraDetails', 'photo', 'telecom', 'coverageArea', 'serviceProvisioningCode', 'eligibility', 'eligibilityNote', 'programName', 'characteristic', 'referralMethod', 'publicKey', 'appointmentRequired', 'availableTime', 'notAvailable','availabilityExceptions')
