from . import models
from rest_framework import serializers

class OnlineSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = models.Online
        fields = ('id', 'name', 'created_at','last_updated')
