from rest_framework import serializers
from hc_practicas.models import Especialidad

class EspecialidadSerializer(serializers.HyperlinkedModelSerializer):
    """
    Serializa una Especialidad
    """
    id = serializers.ReadOnlyField()

    def create(self, validated_data):
        """
        Crea una Especialidad
        :param validated_data: Valores con los cuales crear la Especialidad
        :return: Una nueva instancia de Especialidad
        """
        return Especialidad.objects.create(**validated_data)


    def update(self, instance, validated_data):
        """
        Modifica una Especialidad
        :param instance: Instancia de Especialidad a modificar
        :param validated_data: Nuevos valores con los que modificar Especialidad
        :return: Instancia de Especialidad modificada
        """
        instance.name = validated_data['name']
        instance.description = validated_data['description']
        instance.status = validated_data['status']
        instance.save()
        return instance

    class Meta:
        model = Especialidad
        fields = ('id', 'name', 'description','status')