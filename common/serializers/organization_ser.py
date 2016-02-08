from rest_framework import serializers
from common.models import OrganizationContact, Identifier, ContactPoint, Address, Organization

class OrganizationSerializer(serializers.HyperlinkedModelSerializer):
    """
    Serializador de Organization
    """
    id = serializers.ReadOnlyField()
    identifier = serializers.HyperlinkedRelatedField(
        view_name="common:Identifier-detail",
        queryset=Identifier.objects
    )
    telecom = serializers.HyperlinkedRelatedField(
        view_name="common:ContactPoint-detail",
        queryset=ContactPoint.objects,
        many=True
    )
    address = serializers.HyperlinkedRelatedField(
        view_name="common:Address-detail",
        queryset=Address.objects,
        many=True
    )
    partOf = serializers.HyperlinkedRelatedField(
        view_name="common:Organization-detail",
        queryset=Organization.objects
    )
    contact = serializers.HyperlinkedRelatedField(
        view_name="common:OrganizationContact",
        queryset=OrganizationContact.objects,
        many=True
    )

    def create(self, validated_data):
        """
        Crea un organization
        :param validated_data:
        :return:
        """
        contacts = validated_data.pop('contact')
        addresses = validated_data.pop('address')
        telecoms = validated_data.pop('telecom')

        organization = Organization.objects.create(**validated_data)

        for contact in contacts:
            organization.contact.add(contact)

        for address in addresses:
            organization.address.add(address)

        for telecom in telecoms:
            organization.telecom.add(telecom)
        organization.save()
        return organization

    def update(self, instance, validated_data):
        """
        Modifica un organization
        :param instance:
        :param validated_data:
        :return:
        """
        instance.identifier = validated_data['identifier']
        instance.telecom = validated_data['telecom']
        instance.address = validated_data['address']
        instance.partOf = validated_data['partOf']
        instance.contact = validated_data['contact']
        instance.active = validated_data['active']
        instance.type = validated_data['active']
        instance.name = validated_data['name']
        instance.save()
        return instance


    class Meta:
        model = Organization
        fields = ('id', 'identifier', 'active', 'type', 'name', 'telecom', 'address','partOf', 'contact')