from . import models
from rest_framework import serializers

class FilerSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = models.Filer
        fields = ('id', 'title', 'created_at','size','upload')



