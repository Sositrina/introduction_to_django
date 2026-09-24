from django.shortcuts import redirect, render

from django.core.mail import send_mail

from users.forms import UserRegisterForm, UserLoginForm

from django.contrib.auth import authenticate, login



def register(request):
    """Регистрирует нового пользователя."""
    if request.method == "POST":
        form = UserRegisterForm(request.POST)

        if form.is_valid():
            user = form.save()

            send_mail(
                "Добро пожаловать!",
                "Спасибо за регистрацию на нашем сайте!",
                None,
                [user.email],
            )
            return redirect("home")
    else:
        form = UserRegisterForm()

    return render(request, "users/register.html", {"form": form})


def user_login(request):
    """Авторизует пользователя."""
    if request.method == "POST":
        form = UserLoginForm(request.POST)

        if form.is_valid():
            email = form.cleaned_data["email"]
            password = form.cleaned_data["password"]

            user = authenticate(request, email=email, password=password)

            if user is not None:
                login(request, user)
                return redirect("home")

            form.add_error(None, "Неверный email или пароль.")
    else:
        form = UserLoginForm()

    return render(request, "users/login.html", {"form": form})
