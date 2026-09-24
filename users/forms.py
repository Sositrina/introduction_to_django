from django import forms

from django.contrib.auth.forms import UserCreationForm

from users.models import User


class UserRegisterForm(UserCreationForm):
    """Форма регистрации пользователя."""

    class Meta:
        model = User
        fields = ("email",)

class UserLoginForm(forms.Form):
    """Форма авторизации пользователя."""

    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)