from django.urls import path
from .views import (
    BoardCreateView,
    BoardListView,
    BoardDetailView,
    BoardUpdateView,
    BoardDeleteView,
)

urlpatterns = [
    path('boards/', BoardListView.as_view(), name='board-list'),
    path('boards/create/', BoardCreateView.as_view(), name='board-create'),
    path('boards/<int:pk>/', BoardDetailView.as_view(), name='board-detail'),
    path('boards/<int:pk>/update/', BoardUpdateView.as_view(), name='board-update'),
    path('boards/<int:pk>/delete/', BoardDeleteView.as_view(), name='board-delete'),
]
