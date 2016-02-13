from rest_framework import serializers
from common.models import Person, Identifier, HumanName, ContactPoint, Address, Organization, PersonLink

class PersonSerializer(serializers.HyperlinkedModelSerializer):
    """
    Serializa una person
    """
    id = serializers.ReadOnlyField()

    identifier = serializers.HyperlinkedRelatedField(
        view_name="common:Identifier-detail",
        queryset=Identifier.objects
    )
    name = serializers.HyperlinkedRelatedField(
        view_name="common:HumanName-detail",
        queryset=HumanName.objects
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

    link = serializers.HyperlinkedRelatedField(
        view_name="common:PersonLink-detail",
        queryset=PersonLink.objects,
        many=True
    )

    def create(self, validated_data):
        """
        Crea un Person
        :param validated_data: Valores con los cuales crear el Person
        :return: Una nueva instancia de Person creada
        """
        telecom = validated_data.pop('telecom')
        address = validated_data.pop('address')
        links = validated_data.pop('link')

        person = Person.objects.create(**validated_data)
        for tel in telecom:
            person.telecom.add(tel)

        for addr in address:
            person.address.add(addr)

        for link in links:
            person.link.add(link)

        return person


    def update(self, instance, validated_data):
        """
        Modifica un Person
        :param instance: Instancia de Person a modificar
        :param validated_data: Nuevos valores con los que modificar Person
        :return: Instancia de Person modificada
        """
        instance.identifier = validated_data['identifier']
        instance.name = validated_data['name']
        instance.telecom = validated_data['telecom']
        instance.gender = validated_data['gender']
        instance.birthDate = validated_data['birthDate']
        instance.address = validated_data['address']
        instance.photo = validated_data['photo']
        instance.managingOrganization = validated_data['managingOrganization']
        instance.active = validated_data['active']
        instance.link = validated_data['link']
        instance.save()
        return instance

    class Meta:
        model = Person
        fields = ('id', 'identifier', 'name', 'telecom','gender','birthDate', 'address', 'photo', 'managingOrganization', 'active', 'link')