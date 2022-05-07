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


class DataSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = models.Data
        fields = ('id', 'name', 'created_at','last_updated','data')
    

class Antik_fupSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = models.Antik_fup
        fields = ('date','download','upload')


class MeetingSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = models.Meeting
        fields = ('id','name','link','organizer','time','duration')