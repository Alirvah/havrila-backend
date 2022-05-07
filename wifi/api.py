from . import models
from . import serializers
from rest_framework.response import Response
from rest_framework import viewsets, permissions


class DeviceViewSet(viewsets.ModelViewSet):
    """ViewSet for the Room class"""

    queryset = models.Device.objects.all()
    serializer_class = serializers.DeviceSerializer
    permission_classes = [permissions.IsAuthenticated]


    def create(self,request):
        for i in self.request.data['devices']:
            wifi = models.Device.objects.create(
                   ip=i['ip'],
                   mac=i['mac'],
                   name=i['name']
            )
            wifi.save()
        return Response({'status':'ok'})

    def get_queryset(self):
        if self.request.user.is_staff:
          return models.Device.objects.all()
