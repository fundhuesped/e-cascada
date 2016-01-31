from rest_framework import serializers
from common.models import ContactPointPeriod, ContactPoint

__author__ = 'Santi'

class ContactPointPeriodSerializer(serializers.Serializer):
    """
    Serializador de IdentifierPeriod
    """
    start = serializers.DateTimeField()
    end = serializers.DateTimeField()

    def create(self, validated_data):
        """
        Create an IdentifierPeriod
        :param validated_data:
        :return:
        """
        return ContactPointPeriod.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.start = validated_data.get('start', instance.start)
        instance.end = validated_data.get('end', instance.end)
        instance.save()
        return instance

class ContactPointSerializer(serializers.HyperlinkedModelSerializer):
    """
    Serializa un ContactPoint
    """
    period = ContactPointPeriodSerializer()

    """"
    def create(self, validated_data):
        system = validated_data['system']
        value = validated_data['value']
        use = validated_data['use']
        rank = validated_data['rank']
        periodo = ContactPointPeriod(start = validated_data['period']['start'], end = validated_data['period']['end'])
        periodo.save()
        return ContactPoint.objects.create(system=system, value=value, use=use, rank=rank, period=periodo)

    def update(self, instance, validated_data):
        instance.system = validated_data['system']
        instance.value = validated_data['value']
        instance.use = validated_data['use']
        instance.rank = validated_data['rank']
        instance.period = ContactPointPeriod.objects.get_or_create(start = validated_data['period']['start'], end = validated_data['period']['end'])
        instance.save()
        return instance
    """

    class Meta:
        model = ContactPoint
        fields = ('system', 'value', 'use', 'rank', 'period')
