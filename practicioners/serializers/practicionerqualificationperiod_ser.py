from rest_framework import serializers
from practicioners.models import PracticionerQualificationPeriod

class PracticionerQualificationPeriodSerializer(serializers.HyperlinkedModelSerializer):
    """
    Serializador de PracticionerQualificationPeriod
    """
    id = serializers.ReadOnlyField()
    start = serializers.DateTimeField()
    end = serializers.DateTimeField()

    def create(self, validated_data):
        """
        Create an PracticionerQualificationPeriod
        :param validated_data: Datos con los cuales crear la nueva instancia de PracticionerQualificationPeriod
        :return: La nueva instancia de PracticionerQualificationPeriod
        """
        return PracticionerQualificationPeriod.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Modifica un PracticionerQualificationPeriod
        :param instance: Instancia de PracticionerQualificationPeriod a modificar
        :param validated_data: Datos con los cuales modificar el PracticionerQualificationPeriod
        :return: Instancia modificada de PracticionerQualificationPeriod
        """
        instance.start = validated_data['start']
        instance.end = validated_data['end']
        instance.save()
        return instance

    class Meta:
        model = PracticionerQualificationPeriod
        fields = ('id', 'start', 'end')