from django.shortcuts import render
from .models import Project
from rest_framework import generics
from .models import Board
from .serializers import BoardSerializer
from .permissions import IsOwnerOrReadOnly

def dashboard_view(request):
    projects = Project.objects.filter(owner=request.user)
    return render(request, 'dashboard.html', {'projects': projects})

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
