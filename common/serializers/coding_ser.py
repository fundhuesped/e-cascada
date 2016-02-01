from rest_framework import serializers
from common.models import Coding

class CodingSerializer(serializers.Serializer):
    pk = serializers.IntegerField(read_only=True)
    system = serializers.URLField()
    version = serializers.CharField()
    code = serializers.CharField()
    display = serializers.CharField()
    userSelected = serializers.BooleanField()

    def create(self, validated_data):
        #Create and return a new `Coding` instance, given the validated data.
        return Coding.objects.create(**validated_data)

    def update(self, instance, validated_data):
        #Update and return an existing `Snippet` instance, given the validated data.

        instance.system = validated_data.get('system', instance.system)
        instance.version = validated_data.get('version', instance.version)
        instance.code = validated_data.get('code', instance.code)
        instance.display = validated_data.get('display', instance.display)
        instance.userSelected = validated_data.get('userSelected', instance.userSelected)
        instance.save()
        return instance

