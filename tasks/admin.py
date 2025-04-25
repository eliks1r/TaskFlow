from django.contrib import admin
from .models import Board, Task, Project, TaskList, BoardParticipant

@admin.register(Board)
class BoardAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'owner', 'created_at')
    list_filter = ('owner',)
    search_fields = ('name',)

@admin.register(TaskList)
class TaskListAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'board')
    list_filter = ('board',)
    search_fields = ('name',)

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'created', 'status']
    list_filter = ['status', 'created']
    search_fields = ['title']

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'status', 'progress', 'user')
    list_filter = ('status',)
    search_fields = ('name',)

@admin.register(BoardParticipant)
class BoardParticipantAdmin(admin.ModelAdmin):
    list_display = ['board', 'user', 'role']
    list_filter = ['role']
    search_fields = ['user__username']
