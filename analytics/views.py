from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from tasks.models import Task
from django.db.models import Count
from django.utils.timezone import now
from datetime import timedelta

class TaskAnalyticsView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user

        all_tasks = Task.objects.filter(list__board__owner=user)
        total_tasks = all_tasks.count()
        completed = Task.objects.filter(status='done').count()
        in_progress = all_tasks.filter(status='In Progress').count()
        todo = all_tasks.filter(status='To Do').count()

        # Пример аналитики за последнюю неделю
        week_ago = now() - timedelta(days=7)
        recent_tasks = all_tasks.filter(created__gte=week_ago).count()

        return Response({
            "total_tasks": total_tasks,
            "completed": completed,
            "in_progress": in_progress,
            "todo": todo,
            "last_7_days": recent_tasks
        })
