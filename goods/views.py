from django.shortcuts import render
from django.http import HttpResponse

def catalog(request):
    context: dict[str, str] = {
        'title': 'Home',
        'content': 'Sweet Point - Главная'
    }
    return render(request, 'goods/catalog.html', context)

# может добавлю отзывы
