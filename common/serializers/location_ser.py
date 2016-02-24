from rest_framework import serializers
from common.models import Location, Identifier, ContactPoint, Address, Organization

class LocationSerializer(serializers.HyperlinkedModelSerializer):
    """
    Serializa un Location
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

    managingOrganization = serializers.HyperlinkedRelatedField(
        view_name="common:Organization-detail",
        queryset=Organization.objects
    )
    partOf = serializers.HyperlinkedRelatedField(
        view_name="common:Location-detail",
        queryset=Location.objects,
        allow_null=True
    )

    def create(self, validated_data):
        """
        Crea un Location
        :param validated_data: Valores con los cuales crear el Location
        :return: Una nueva instancia de Location creada
        """
        telecom = validated_data.pop('telecom')
        address = validated_data.pop('address')

        location = Location.objects.create(**validated_data)
        for tel in telecom:
            location.telecom.add(tel)
        for add in address:
            location.address.add(add)

        return location


    def update(self, instance, validated_data):
        """
        Modifica un Location
        :param instance: Instancia de Location a modificar
        :param validated_data: Nuevos valores con los que modificar Location
        :return: Instancia de Location modificada
        """
        instance.identifier = validated_data['identifier']
        instance.status = validated_data['status']
        instance.name = validated_data['name']
        instance.description = validated_data['description']
        instance.mode = validated_data['mode']
        instance.type = validated_data['type']
        instance.telecom = validated_data['telecom']
        instance.address = validated_data['address']
        instance.physicalType = validated_data['physicalType']
        instance.positionLongitude = validated_data['positionLongitude']
        instance.positionLatitude = validated_data['positionLatitude']
        instance.positionAltitude = validated_data['positionAltitude']
        instance.managingOrganization = validated_data['managingOrganization']
        instance.partOf = validated_data['partOf']
        instance.save()
        return instance

    class Meta:
        model = Location
        fields = ('id', 'identifier', 'status', 'name', 'description', 'mode', 'type', 'telecom', 'address', 'physicalType', 'positionLongitude', 'positionLatitude', 'positionAltitude', 'managingOrganization', 'partOf')
