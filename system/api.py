from . import models
from . import serializers
from rest_framework.response import Response
from rest_framework import viewsets, permissions
from helpers.permissions import FastTokenAllow


class OnlineViewSet(viewsets.ModelViewSet):
    """ViewSet for the Room class"""

    queryset = models.Online.objects.all()
    serializer_class = serializers.OnlineSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        return self.queryset.first()

class Server_logViewSet(viewsets.ModelViewSet):
    """ViewSet for the Room class"""

    queryset = models.Server_log.objects.all()
    serializer_class = serializers.Server_logSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        if 'server' in self.request.query_params:
            return models.Server_log.objects.filter(
                server=self.request.query_params['server']
            )[:10]


class DataViewSet(viewsets.ModelViewSet):
    """ViewSet for the Room class"""

    queryset = models.Data.objects.all()
    serializer_class = serializers.DataSerializer
    permission_classes = [permissions.IsAuthenticated]


class Antik_fupViewSet(viewsets.ModelViewSet):
    """ViewSet for the Room class"""

    queryset = models.Antik_fup.objects.all()
    serializer_class = serializers.Antik_fupSerializer
    permission_classes = [permissions.IsAuthenticated]

    def create(self, request, *args, **kwargs):
        if 'data' in request.data:
            serializer = self.get_serializer(data=request.data['data'], many=True)
            for o in request.data['data']:
                fup, created = models.Antik_fup.objects.get_or_create(
                    date = o['date'],
                    download = o['download'],
                    upload = o['upload'],
                )
                if created:
                    fup.save()
            return Response(request.data['data'])
        return Response(request.data, status=400)

    def get_queryset(self):
        if self.request.user.is_staff:
          return models.Antik_fup.objects.all()[:30]


class MeetingViewSet(viewsets.ModelViewSet):
    """ViewSet for the Room class"""

    queryset = models.Meeting.objects.all()
    serializer_class = serializers.MeetingSerializer
    permission_classes = [permissions.IsAuthenticated|FastTokenAllow]

    def create(self, request, *args, **kwargs):
        serializer = serializers.MeetingSerializer(data=request.data)
        if serializer.is_valid():
            meeting, created = models.Meeting.objects.update_or_create(
                name=request.data['name'],
                link=request.data['link'],
                organizer=request.data['organizer'],
                time=request.data['time'],
                duration=request.data['duration']
            )
            return Response(request.data)
        return Response(request.data, status=400)
    
    def get_queryset(self):
        return models.Meeting.objects.all()[:10]
