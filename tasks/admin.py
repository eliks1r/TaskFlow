
from django.contrib import admin
from .models import Board, List, Task

@admin.register(Board)
class BoardAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'owner', 'created_at')
    list_filter = ('owner',)
    search_fields = ('name',)

@admin.register(List)
class ListAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'board', 'position')
    list_filter = ('board',)
    search_fields = ('name',)

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'list', 'due_date', 'position', 'created_at')
    list_filter = ('list', 'due_date')
    search_fields = ('title', 'description')
