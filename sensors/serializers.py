from . import models
from rest_framework import serializers

class SensorSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = models.Sensor
        fields = ('id', 'ts', 'broadband','infrared','light','temprpi','temproom','pressure','humidity')


class StatusSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = models.Status
        fields = ('id', 'ts', 'uptime','cpu','mem','disk','temp','wrec','wtran')
