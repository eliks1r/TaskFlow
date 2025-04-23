from django.urls import path
from .views import TaskAnalyticsView

urlpatterns = [
    path('tasks-summary/', TaskAnalyticsView.as_view(), name='task-analytics'),
]
