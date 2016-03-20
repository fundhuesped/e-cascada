from rest_framework import serializers
from hc_common.models import Persona
from hc_common.serializers import DocumentoNestedSerializer

class PersonaNestSerializer(serializers.ModelSerializer):
    """
    Serializa una Persona
    """
    id = serializers.ReadOnlyField()

    documento = DocumentoNestedSerializer(
        many=False,
        read_only=True
    )

    def create(self, validated_data):
        persona = Persona.objects.create(
            firstName = validated_data.get('firstName'),
            otherNames = validated_data.get('otherNames'),
            fatherSurname = validated_data.get('fatherSurname'),
            motherSurname = validated_data.get('motherSurname'),
            birthDate = validated_data.get('birthDate'),
        )

        return persona

    def update(self, instance, validated_data):
        instance.firstName= validated_data.get('firstName', instance.firstName)
        instance.otherNames = validated_data.get('otherNames', instance.otherNames)
        instance.fatherSurname = validated_data.get('fatherSurname', instance.fatherSurname)
        instance.motherSurname = validated_data.get('motherSurname', instance.motherSurname)
        instance.birthDate = validated_data.get('birthDate', instance.birthDate)
        instance.save()

        return instance


    class Meta:
        model = Persona
        fields = ('id', 'firstName', 'otherNames', 'fatherSurname', 'motherSurname', 'documento', 'birthDate')