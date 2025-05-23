from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    context: dict[str, str] = {
        'title': 'Home',
        'content': 'Sweet Point - Главная'
    }

    return render(request, 'main/index.html', context)

def about(request):
    context: dict[str, str] = {
        'title': 'О нас',
        'content': 'Sweet Point - О нас'
    }

    return render(request, 'main/about.html', context)
