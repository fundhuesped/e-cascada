from rest_framework import serializers
from common.models import AddressPointPeriod, AddressLine, Address

class AddressSerializer(serializers.HyperlinkedModelSerializer):
    """
    Serializa un Address
    """
    id = serializers.ReadOnlyField()

    period = serializers.HyperlinkedRelatedField(
        view_name="common:AddressPointPeriod-detail",
        queryset=AddressPointPeriod.objects
    )

    lines = serializers.HyperlinkedRelatedField(
        view_name="common:AddressLine-detail",
        queryset=AddressLine.objects,
        many=True
    )

    def create(self, validated_data):
        """
        Crea un Address
        :param validated_data: Valores con los cuales crear el Address
        :return: Una nueva instancia de Address creada
        """
        lines = validated_data.pop('lines')
        addr = Address.objects.create(**validated_data)
        for line in lines:
            addr.lines.add(line)
        return addr


    def update(self, instance, validated_data):
        """
        Modifica un Address
        :param instance: Instancia de Address a modificar
        :param validated_data: Nuevos valores con los que modificar Address
        :return: Instancia de Address modificada
        """
        instance.use = validated_data['use']
        instance.type = validated_data['type']
        instance.text = validated_data['text']
        instance.lines = validated_data['lines']
        instance.city = validated_data['city']
        instance.district = validated_data['district']
        instance.state = validated_data['state']
        instance.postalCode = validated_data['postalCode']
        instance.country = validated_data['country']
        instance.period = validated_data['period']
        instance.save()
        return instance

    class Meta:
        model = Address
        fields = ('id', 'use', 'type', 'text', 'lines', 'city', 'district', 'state', 'postalCode', 'country', 'period')
