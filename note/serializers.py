from . import models
from rest_framework import serializers

class NoteSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = models.Note
        fields = ('id', 'title', 'content', 'created_at', 'created_by', 'starred')

