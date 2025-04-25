from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),  # Путь к административной панели Django
    path('auth/', include('users.urls')),  # Подключение пользователей
    path('boards/', views.BoardListView.as_view(), name='board-list'),
    path('boards/create/', views.BoardCreateView.as_view(), name='board-create'),
    path('boards/<int:pk>/', views.BoardDetailView.as_view(), name='board-detail'),
    path('boards/<int:pk>/update/', views.BoardUpdateView.as_view(), name='board-update'),
    path('boards/<int:pk>/delete/', views.BoardDeleteView.as_view(), name='board-delete'),

    path('tasks/', views.TaskListView.as_view(), name='task-list'),
    path('tasks/create/', views.TaskCreateView.as_view(), name='task-create'),
    path('tasks/<int:pk>/', views.TaskDetailView.as_view(), name='task-detail'),
    path('tasks/<int:pk>/update/', views.TaskUpdateView.as_view(), name='task-update'),
    path('tasks/<int:pk>/delete/', views.TaskDeleteView.as_view(), name='task-delete'),

    path('analytics/', views.TaskAnalyticsView.as_view(), name='task-analytics'),
    path('ai/generate-description/', views.AIDescriptionView.as_view(), name='ai-generate-description'),
]

