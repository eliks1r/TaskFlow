# users/views.py
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from .forms import RegisterForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required


# Представление для регистрации
def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Логиним пользователя сразу после регистрации
            return redirect('home')  # Перенаправляем на главную страницу после регистрации
    else:
        form = RegisterForm()
    return render(request, 'users/register.html', {'form': form})

# Представление для логина
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')  # Перенаправляем на главную страницу после логина
    else:
        form = AuthenticationForm()
    return render(request, 'users/login.html', {'form': form})

# Представление для выхода
def logout_view(request):
    logout(request)
    return redirect('login')  # Перенаправляем на страницу логина после выхода


from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Представление для главной страницы (личного кабинета)
@login_required
def home_view(request):
    return render(request, 'home.html')  # Отображаем главную страниц

@login_required
def task_view(request):
    return render(request, 'users/task.html')  # Убедитесь, что путь верен

@login_required
def profile_view(request):
    return render(request, 'users\profile.html')

