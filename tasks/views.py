from rest_framework import generics
from .models import Board, Task
from .serializers import BoardSerializer, TaskSerializer
from .permissions import IsOwnerOrReadOnly
from rest_framework.views import APIView
from rest_framework.response import Response
import openai
import os

class BoardCreateView(generics.CreateAPIView):
    queryset = Board.objects.all()
    serializer_class = BoardSerializer

class BoardListView(generics.ListAPIView):
    queryset = Board.objects.all()
    serializer_class = BoardSerializer

class BoardDetailView(generics.RetrieveAPIView):
    queryset = Board.objects.all()
    serializer_class = BoardSerializer

class BoardUpdateView(generics.UpdateAPIView):
    queryset = Board.objects.all()
    serializer_class = BoardSerializer
    permission_classes = [IsOwnerOrReadOnly]

class BoardDeleteView(generics.DestroyAPIView):
    queryset = Board.objects.all()
    serializer_class = BoardSerializer
    permission_classes = [IsOwnerOrReadOnly]

class TaskListView(generics.ListAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

class TaskCreateView(generics.CreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    
class TaskDetailView(generics.RetrieveAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    
class TaskUpdateView(generics.UpdateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

class TaskDeleteView(generics.DestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    
class AIDescriptionView(APIView):
    def post(self, request):
        title = request.data.get("title", "")
        if not title:
            return Response({"error": "title is required"}, status=400)
        description = generate_task_description(title)
        return Response({"title": title, "description": description})