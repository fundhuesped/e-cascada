from rest_framework import serializers
from hc_common.models import Documento
from hc_common.serializers import PersonaNestedSerializer

class DocumentoNestSerializer(serializers.ModelSerializer):
    """
    Serializa un Documento
    """
    id = serializers.ReadOnlyField()

    persona = PersonaNestedSerializer(
        many=False
    )

    def create(self, validated_data):
        persona = validated_data.pop('persona')
        documento = Documento.objects.create(
            type = validated_data.get('type'),
            number = validated_data.get('number'),
            comments = validated_data.get('comments'),
            persona = persona
        )

        return documento

    def update(self, instance, validated_data):
        persona = validated_data.pop('persona')
        instance.type= validated_data.get('type', instance.type)
        instance.number = validated_data.get('number', instance.number)
        instance.comments = validated_data.get('comments', instance.comments)
        instance.persona = persona
        instance.save()

        return instance


    class Meta:
        model = Documento
        fields = ('id', 'type', 'number', 'comments', 'persona')