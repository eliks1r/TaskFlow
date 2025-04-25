from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home_view, name='home'),
    path('register/', views.register_view, name='register'),  # Убедитесь, что путь для регистрации правильный
    path('login/', views.login_view, name='login'),
]
