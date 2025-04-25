# users/views.py
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from .forms import RegisterForm
from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import RegisterForm

# Представление для регистрации
def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()  # Сохраняем нового пользователя
            login(request, user)  # Логиним пользователя
            return redirect('home')  # Перенаправляем на главную страницу после регистрации
    else:
        form = RegisterForm()  # Отображаем пустую форму для регистрации
    return render(request, 'users/register.html', {'form': form})

# Представление для логина
def login_view(request):  
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)  # Вход пользователя
            next_url = request.GET.get('next', 'home')  # Если в запросе есть 'next', перенаправляем туда
            return redirect(next_url)  # Редирект на 'home' или страницу из 'next'
    else:
        form = AuthenticationForm()  # Если это GET-запрос, показываем форму
    return render(request, 'users/login.html', {'form': form})

# Представление для выхода из системы
def logout_view(request):
    logout(request)  # Выход из системы
    return redirect('login')  # Перенаправление на страницу логина после выхода


# Представление для страницы 404
def custom_404(request, exception):
    return render(request, '404.html', {'message': 'Page not found'}, status=404)

@login_required
def home_view(request):
    return render(request, 'home.html')  # Отображаем главную страницу

def logout_view(request):
    logout(request)  # Выход пользователя
    return redirect('login')  # Перенаправление на страницу логина