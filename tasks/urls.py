from django.urls import path
from .views import (
    BoardCreateView,
    BoardListView,
    BoardDetailView,
    BoardUpdateView,
    BoardDeleteView,
    TaskListView,
    TaskCreateView,
    TaskDetailView,
    TaskUpdateView,
    TaskDeleteView,
    AIDescriptionView,
)

urlpatterns = [
    path('boards/', BoardListView.as_view(), name='board-list'),
    path('boards/create/', BoardCreateView.as_view(), name='board-create'),
    path('boards/<int:pk>/', BoardDetailView.as_view(), name='board-detail'),
    path('boards/<int:pk>/update/', BoardUpdateView.as_view(), name='board-update'),
    path('boards/<int:pk>/delete/', BoardDeleteView.as_view(), name='board-delete'),

    path('tasks/', TaskListView.as_view(), name='task-list'),
    path('tasks/create/', TaskCreateView.as_view(), name='task-create'),
    path('tasks/<int:pk>/', TaskDetailView.as_view(), name='task-detail'),
    path('tasks/<int:pk>/update/', TaskUpdateView.as_view(), name='task-update'),
    path('tasks/<int:pk>/delete/', TaskDeleteView.as_view(), name='task-delete'),
]

urlpatterns += [
    path('ai/generate-description/', AIDescriptionView.as_view(), name='ai-generate-description'),
]