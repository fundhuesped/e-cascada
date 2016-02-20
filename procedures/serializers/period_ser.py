from rest_framework import serializers
from procedures.models import Period

class PeriodSerializer(serializers.HyperlinkedModelSerializer):
    """
    Serializa un Period
    """
    id = serializers.ReadOnlyField()

    def create(self, validated_data):
        """
        Crea un Period
        :param validated_data: Valores con los cuales crear el Period
        :return: Una nueva instancia de Period
        """
        return Period.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Modifica un Period
        :param instance: Instancia de Period a modificar
        :param validated_data: Nuevos valores con los que modificar Period
        :return: Instancia de Period modificada
        """
        instance.start = validated_data['start']
        instance.end = validated_data['end']
        instance.save()
        return instance

    class Meta:
        model = Period
        fields = ('id', 'start', 'end')
