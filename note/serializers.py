from . import models
from rest_framework import serializers

class NotebookSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = models.Notebook
        fields = ('id', 'title', 'created_at')


class NoteSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = models.Note
        fields = ('id', 'title','content', 'created_at','starred','notebook')
