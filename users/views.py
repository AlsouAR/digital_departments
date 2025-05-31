from django.shortcuts import render

# Create your views here.

def login(request):
    context: dict[str, str] = {
        'title': 'Sweet Point - Авторизация',
    }

    return render(request, 'users/login.html', context)

def profile(request):
    context: dict[str, str] = {
        'title': 'Sweet Point - Профиль',
    }

    return render(request, 'users/profile.html', context)

def registration(request):
    context: dict[str, str] = {
        'title': 'Sweet Point - Регистрация',
    }

    return render(request, 'users/registration.html', context)

def logout(request):
    ...
