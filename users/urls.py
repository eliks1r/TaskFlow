from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from users.views import calendar_tasks
from .views import calendar_view, calendar_tasks


urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
    path('home/', views.home_view, name='home'),
    path('profile/', views.profile_view, name='profile'),
    path('tasks/', views.task_view, name='task'),  # Путь для задач
    path('calendar/', calendar_view, name='calendar'),
    path('api/calendar-tasks/', calendar_tasks, name='calendar_tasks'),
    path("pomodoro/", views.pomodoro_view, name="pomodoro"),

]

