from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import CustomUser

class RegisterForm(UserCreationForm):
    email = forms.EmailField()
    full_name = forms.CharField()

    class Meta:
        model = CustomUser
        fields = ['full_name', 'email', 'password1', 'password2']

class LoginForm(AuthenticationForm):
    username = forms.EmailField(label="Email")
