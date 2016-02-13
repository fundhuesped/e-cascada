from rest_framework import serializers
from common.models import PersonLink

class PersonLinkSerializer(serializers.HyperlinkedModelSerializer):
    """
    Serializer de PersonLink
    """
    id = serializers.ReadOnlyField()

    def update(self, instance, validated_data):
        """
        Modifica un PersonLink
        :param instance: Instancia de PersonLink a modificar
        :param validated_data: Nuevos valores con los que modificar PersonLink
        :return: Instancia de PersonLink modificada
        """
        instance.target = validated_data['target']
        instance.assurance = validated_data['assurance']
        instance.save()
        return instance

    class Meta:
        model = PersonLink
        fields = ('id', 'target', 'assurance')