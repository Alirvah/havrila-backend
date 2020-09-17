from . import models
from rest_framework import serializers

class TodoSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = models.Todo
        fields = ('id', 'title', 'created_at','done')


