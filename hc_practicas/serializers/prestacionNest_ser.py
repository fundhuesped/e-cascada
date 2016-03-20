from rest_framework import serializers
from hc_practicas.models import Prestacion, Especialidad
from hc_practicas.serializers import EspecialidadNestedSerializer

class PrestacionNestSerializer(serializers.ModelSerializer):
    """
    Serializa una Prestación
    """
    id = serializers.ReadOnlyField()

    especialidad = EspecialidadNestedSerializer(
        many=False
    )

    def create(self, validated_data):
        especialidad = validated_data.pop('especialidad')
        prestacion = Prestacion.objects.create(
            name = validated_data.get('name'),
            description = validated_data.get('description'),
            status = validated_data.get('status'),
            duration = validated_data.get('duration'),
            default = validated_data.get('default'),
            notes = validated_data.get('notes'),
            especialidad = especialidad
        )

        return prestacion

    def update(self, instance, validated_data):
        especialidad = validated_data.pop('especialidad')
        instance.name= validated_data.get('name', instance.name)
        instance.description = validated_data.get('description', instance.description)
        instance.status = validated_data.get('status', instance.status)
        instance.duration = validated_data.get('duration', instance.duration)
        instance.default = validated_data.get('default', instance.duration)
        instance.notes = validated_data.get('notes', instance.notes)
        instance.especialidad = especialidad
        instance.save()

        return instance


    class Meta:
        model = Prestacion
        fields = ('id', 'name', 'description', 'status', 'duration', 'default', 'notes', 'especialidad')