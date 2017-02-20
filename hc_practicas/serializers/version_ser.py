from reversion.models import Version
from hc_practicas.models import Turno
from rest_framework import serializers


class VersionSerializer(serializers.Serializer):
    class Meta:
        model = Turno
        fields = ('taken')
