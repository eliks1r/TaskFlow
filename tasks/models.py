from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser  

class TaskList(models.Model):
    name = models.CharField(max_length=255)
    # сюда можно добавить поле board, если оно у тебя есть

    def __str__(self):
        return self.name

class Task(models.Model):
    list = models.ForeignKey(TaskList, on_delete=models.CASCADE, related_name='tasks')
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

class Board(models.Model):
    name = models.CharField(max_length=100)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='boards')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Project(models.Model):
    name = models.CharField(max_length=100)
    status = models.CharField(max_length=30, default="To Do")
    progress = models.PositiveIntegerField(default=0)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class List(models.Model):
    name = models.CharField(max_length=255)
    board = models.ForeignKey(Board, on_delete=models.CASCADE, related_name='lists')
    position = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"{self.name} ({self.board.name})"


class BoardParticipant(models.Model):
    class Role(models.IntegerChoices):
        OWNER = 1, 'Владелец'
        PARTICIPANT = 2, 'Участник'

    board = models.ForeignKey(Board, on_delete=models.CASCADE, related_name='participants')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    role = models.PositiveSmallIntegerField(choices=Role.choices)

    class Meta:
        unique_together = ('board', 'user')


