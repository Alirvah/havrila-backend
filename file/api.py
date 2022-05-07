from . import models
from . import serializers
from rest_framework.response import Response
from rest_framework import viewsets, permissions

import boto3
from django.conf import settings


class FilerViewSet(viewsets.ModelViewSet):
    """ViewSet for the Room class"""

    queryset = models.Filer.objects.all()
    serializer_class = serializers.FilerSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        #s3 = boto3.client('s3')

        #fs = models.Filer.objects.filter(created_by=self.request.user)
        #for f in fs:
        #  url = s3.generate_presigned_url('get_object',
        #       Params={
        #           'Bucket': settings.S3_BUCKET,
        #           'Key': f.title,
        #       },                       
        #       ExpiresIn=3600)
        #  f.path = url
        #  f.save()
        return models.Filer.objects.filter(created_by=self.request.user)

    def create(self,request):
        filer = models.Filer.objects.create(
            upload=self.request.FILES.get('upload'),
            created_by = self.request.user
        )
        filer.save()
        return Response({'status':'ok','id':filer.id})

    def destroy(self, request, *args, **kwargs):
        f = self.get_object()
        client = boto3.client('s3')
        client.delete_object(Bucket=settings.S3_BUCKET, Key=f.title)
        f.delete()
        return Response({'status':'deleted'})



