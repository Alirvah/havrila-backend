from . import models
from . import serializers
from rest_framework.response import Response
from rest_framework import viewsets, permissions


class SensorViewSet(viewsets.ModelViewSet):
    """ViewSet for the Room class"""

    queryset = models.Sensor.objects.all()
    serializer_class = serializers.SensorSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        if self.request.user.is_staff:
          return models.Sensor.objects.all()[:10000]



class StatusViewSet(viewsets.ModelViewSet):
    """ViewSet for the Room class"""

    queryset = models.Status.objects.all()
    serializer_class = serializers.StatusSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        if self.request.user.is_staff:
          return models.Status.objects.all()[:10000]


