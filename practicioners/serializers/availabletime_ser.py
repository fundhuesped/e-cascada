from rest_framework import serializers
from practicioners.models import AvailableTime
from common.models import DayOfWeek

class AvailableTimeSerializer(serializers.HyperlinkedModelSerializer):
    """
    Serializa un AvailableTime
    """
    id = serializers.ReadOnlyField()
    daysOfWeek = serializers.HyperlinkedRelatedField(
        view_name="common:DayOfWeek-detail",
        queryset=DayOfWeek.objects,
        many=True
    )
    def create(self, validated_data):
        """
        Crea un AvailableTime
        :param validated_data: Valores con los cuales crear el AvailableTime
        :return: Una nueva instancia de AvailableTime
        """
        days = validated_data.pop('daysOfWeek')
        atime = AvailableTime.objects.create(**validated_data)
        for day in days:
            atime.daysOfWeek.add(day)
        atime.save()
        return atime


    def update(self, instance, validated_data):
        """
        Modifica un AvailableTime
        :param instance: Instancia de AvailableTime a modificar
        :param validated_data: Nuevos valores con los que modificar AvailableTime
        :return: Instancia de AvailableTime modificada
        """
        instance.daysOfWeek = validated_data['daysOfWeek']
        instance.allDay = validated_data['allDay']
        instance.availableStartTime = validated_data['availableStartTime']
        instance.availableEndTime = validated_data['availableEndTime']
        instance.save()
        return instance

    class Meta:
        model = AvailableTime
        fields = ('id', 'daysOfWeek', 'allDay', 'availableStartTime', 'availableEndTime')