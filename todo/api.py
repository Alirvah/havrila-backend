from . import models
from . import serializers
from rest_framework.response import Response
from rest_framework import viewsets, permissions


class TodoViewSet(viewsets.ModelViewSet):
    """ViewSet for the Room class"""

    queryset = models.Todo.objects.all()
    serializer_class = serializers.TodoSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return models.Todo.objects.filter(created_by=self.request.user)

    def create(self,request):
        todo = models.Todo.objects.create(
            title=self.request.data['title'],
            created_by = self.request.user
        )
        todo.save()
        return Response({'status':'ok','id':todo.id})


