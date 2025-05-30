from unicodedata import category
from django.http import HttpResponse
from django.shortcuts import render

from goods.models import Categories

def index(request):


    context: dict[str, str] = {
        'title': 'Home',
        'content': 'Sweet Point - Главная',
    }

    return render(request, 'main/index.html', context)

def about(request):
    context: dict[str, str] = {
        'title': 'О нас',
        'content': 'Sweet Point - О нас'
    }

    return render(request, 'main/about.html', context)

def contacts(request):
    context: dict[str, str] = {
        'title': 'Контакты',
        'content': 'Sweet Point - Контакты'
    }

    return render(request, 'main/contacts.html', context)

def delivery(request):
    context: dict[str, str] = {
        'title': 'Доставка и оплата',
        'content': 'Sweet Point - Доставка и оплата'
    }

    return render(request, 'main/delivery.html', context)
