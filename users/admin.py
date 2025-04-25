# users/admin.py

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, CustomUserGroup

# Настройка отображения кастомной модели пользователя
class CustomUserAdmin(UserAdmin):
    model = CustomUser
    
    # Поля для отображения в админке
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name', 'email', 'full_name')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )
    
    # Используем filter_horizontal для отображения ManyToMany полей
    filter_horizontal = ('groups', 'user_permissions')

    # Для отображения полей в списке (если нужно)
    list_display = ('username', 'first_name', 'last_name', 'email', 'is_active', 'is_staff')

# Регистрируем кастомного пользователя в админке
admin.site.register(CustomUser, CustomUserAdmin)

# Регистрируем промежуточную модель CustomUserGroup для связи с группами
@admin.register(CustomUserGroup)
class CustomUserGroupAdmin(admin.ModelAdmin):
    list_display = ['user', 'group']  # Отображаем пользователя и группу в админке
