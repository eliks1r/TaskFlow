from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import CustomUser
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser  # Убедитесь, что импортируете CustomUser
from django.contrib.auth.forms import AuthenticationForm
from django import forms


class LoginForm(AuthenticationForm):
    username = forms.EmailField(label="Email")

class CustomUserCreationForm(UserCreationForm):
    # Добавьте любые дополнительные поля, если нужно
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')  # Поля для формы

class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password1', 'password2']
        
class RegisterForm(UserCreationForm):
    class Meta:
        model = CustomUser  # Используйте CustomUser вместо User
        fields = ['username', 'email', 'full_name', 'password1', 'password2']
        
class LoginForm(AuthenticationForm):
    username = forms.EmailField(label="Email")
    password = forms.CharField(label="Password", widget=forms.PasswordInput)