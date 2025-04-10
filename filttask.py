from django.db import models
from django.contrib.auth.models import User

class Task(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('in_progress', 'In Progress'),
        ('completed', 'Completed'),
    ]
    title = models.CharField(max_length=255)
    description = models.TextField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    priority = models.IntegerField(default=1)
    deadline = models.DateTimeField()
    assigned_to = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tasks')
    tags = models.ManyToManyField('Tag', blank=True)

class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)