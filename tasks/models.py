from django.db import models
from django.conf import settings

# TaskList Model
class TaskList(models.Model):
    name = models.CharField(max_length=255)
    board = models.ForeignKey('Board', on_delete=models.CASCADE, related_name='task_lists')

    def __str__(self):
        return self.name

# Task Model
class Task(models.Model):
    task_list = models.ForeignKey(TaskList, on_delete=models.CASCADE, related_name='tasks')
    task_list = models.ForeignKey(TaskList, on_delete=models.CASCADE) 
    title = models.CharField(max_length=255)
    created = models.DateTimeField(auto_now_add=True)
    status = models.CharField(
        max_length=20,
        choices=[
            ('todo', 'To Do'),
            ('in_progress', 'In Progress'),
            ('done', 'Done'),
        ],
        default='todo'
    )

    def __str__(self):
        return self.title

# Board Model
class Board(models.Model):
    name = models.CharField(max_length=100)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='boards')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

# Project Model
class Project(models.Model):
    name = models.CharField(max_length=100)
    status = models.CharField(max_length=30, default="To Do")
    progress = models.PositiveIntegerField(default=0)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

# BoardParticipant Model
class BoardParticipant(models.Model):
    class Role(models.IntegerChoices):
        OWNER = 1, 'Владелец'
        PARTICIPANT = 2, 'Участник'

    board = models.ForeignKey('tasks.Board', on_delete=models.CASCADE, related_name='tasks_participants')  # Указан полный путь
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='tasks_boardparticipant_set')
    role = models.PositiveSmallIntegerField(choices=Role.choices)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['board', 'user'], name='unique_board_participant_tasks')  # Уникальное имя для задачи
        ]

    def __str__(self):
        return f"{self.user.username} ({self.get_role_display()})"