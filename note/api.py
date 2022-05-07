from . import models
from . import serializers
from rest_framework.response import Response
from rest_framework import viewsets, permissions


class NotebookViewSet(viewsets.ModelViewSet):
    """ViewSet for the Room class"""

    queryset = models.Notebook.objects.all()
    serializer_class = serializers.NotebookSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return models.Notebook.objects.filter(created_by=self.request.user)

    def create(self,request):
        notebook = models.Notebook.objects.create(
            title=self.request.data['title'],
            created_by = self.request.user
        )
        notebook.save()
        return Response({'status':'ok','id':notebook.id})


class NoteViewSet(viewsets.ModelViewSet):
    """ViewSet for the Room class"""

    queryset = models.Note.objects.all()
    serializer_class = serializers.NoteSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        if 'notebook' in self.request.GET:
          return models.Note.objects.filter(notebook=self.request.GET['notebook'])
        else:  
          return models.Note.objects.filter(notebook__created_by=self.request.user.id)

