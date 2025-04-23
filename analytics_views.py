from django.shortcuts import render
from .models import Task

def analytics_view(request):
    # Пример: количество задач по статусу
    status_counts = Task.objects.values('status').annotate(count=models.Count('id'))
    return render(request, 'analytics.html', {'status_counts': status_counts})