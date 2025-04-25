# taskflow_backend/urls.py
from django.contrib import admin
from django.urls import path, include
from users.views import login_view, register_view, home_view, logout_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/login/', login_view, name='login'),
    path('auth/register/', register_view, name='register'),
    path('home/', home_view, name='home'),  # Это URL для главной страницы
    path('auth/logout/', logout_view, name='logout'),  # Путь для выхода
    path('auth/', include('users.urls')),  # Убедитесь, что это добавлено

]
