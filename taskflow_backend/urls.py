# taskflow_backend/urls.py
from django.contrib import admin
from django.urls import path, include
from users.views import login_view, home_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/login/', login_view, name='login'),  # Страница для входа
    path('home/', home_view, name='home'),  # Главная страница
    path('admin/', admin.site.urls),
    path('auth/', include('users.urls')),
    # другие маршруты
]
