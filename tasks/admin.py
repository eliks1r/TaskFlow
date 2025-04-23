from django.contrib import admin
from .models import Board, List, Task, Project
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Task


@admin.register(Board)
class BoardAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'owner', 'created_at')
    list_filter = ('owner',)
    search_fields = ('name',)

@admin.register(List)
class ListAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'board')  # убрала position
    list_filter = ('board',)
    search_fields = ('name',)

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'status', 'progress', 'user')
    list_filter = ('status',)
    search_fields = ('name',)

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'created', 'status']  # исправлено: created вместо created_at
    list_filter = ['created', 'status']
