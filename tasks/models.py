from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Board(models.Model):
    name = models.CharField(max_length=100)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='boards')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Project(models.Model):
    name = models.CharField(max_length=100)
    status = models.CharField(max_length=30, default="To Do")
    progress = models.PositiveIntegerField(default=0)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class List(models.Model):
    name = models.CharField(max_length=255)
    board = models.ForeignKey(Board, on_delete=models.CASCADE, related_name='lists')
    position = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"{self.name} ({self.board.name})"

class Task(models.Model):
    list = models.ForeignKey('List', on_delete=models.CASCADE, related_name='tasks')
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    due_date = models.DateField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    
    # Добавляем вложение файла:
    attachment = models.FileField(upload_to='attachments/', blank=True, null=True)
    def __str__(self):
        return self.title
class BoardParticipant(models.Model):
    class Role(models.IntegerChoices):
        OWNER = 1, 'Владелец'
        PARTICIPANT = 2, 'Участник'

    board = models.ForeignKey(Board, on_delete=models.CASCADE, related_name='participants')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    role = models.PositiveSmallIntegerField(choices=Role.choices)

    class Meta:
        unique_together = ('board', 'user')
