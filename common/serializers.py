from rest_framework import serializers
from common.models import Coding, IdentifierType, IdentifierPeriod, ContactPointPeriod, AddressPointPeriod, NamePeriod, AddressLine


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

class IdentifierTypeSerializer(serializers.Serializer):
    """
    Serializador de un IdentifierType
    """
    pk = serializers.IntegerField(read_only=True)
    coding = serializers.CharField(max_length=4)
    text = serializers.CharField()

    def create(self, validated_data):
        """
        Create the IdentifierType
        :param validated_data:
        :return:
        """
        return IdentifierType.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.coding = validated_data.get('coding', instance.coding)
        instance.text = validated_data.get('text', instance.text)
        instance.save()
        return instance

class IdentifierPeriodSerializer(serializers.Serializer):
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
        return IdentifierPeriod.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.start = validated_data.get('start', instance.start)
        instance.end = validated_data.get('end', instance.end)
        instance.save()
        return instance

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

class AddressPointPeriodSerializer(serializers.Serializer):
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
        return AddressPointPeriod.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.start = validated_data.get('start', instance.start)
        instance.end = validated_data.get('end', instance.end)
        instance.save()
        return instance

class NamePeriodSerializer(serializers.Serializer):
    """
    Serializador de NamePeriod
    """
    start = serializers.DateTimeField()
    end = serializers.DateTimeField()

    def create(self, validated_data):
        """
        Create an NamePeriod
        :param validated_data:
        :return:
        """
        return NamePeriod.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.start = validated_data.get('start', instance.start)
        instance.end = validated_data.get('end', instance.end)
        instance.save()
        return instance

class AddressLineSerializer(serializers.Serializer):
    """
    Serializa un AddressLine
    """
    line = serializers.CharField()

    def create(self, validated_data):
        """
        Create an AddresLine
        :param validated_data:
        :return:
        """
        return AddressLine.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Modifica y devuelve una instancia de AddressLine
        :param instance:
        :param validated_data: Datos validos para crear AddressLine
        :return: Instancia de AddressLine
        """
        instance.line = validated_data.get('line', instance.line)
        instance.save()
        return instance