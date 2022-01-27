from . import models
from rest_framework import serializers

class OnlineSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = models.Online
        fields = ('id', 'name', 'created_at','last_updated')


class Server_logSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = models.Server_log
        fields = ('id', 'name', 'created_at','last_updated','user','operation','server')