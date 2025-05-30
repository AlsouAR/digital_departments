from typing import Any
from unicodedata import category
from django.shortcuts import render
from django.http import HttpResponse

from goods.models import Products


def catalog(request, category_slug=None):
    if category_slug and category_slug != 'all':
        goods = Products.objects.filter(category__slug=category_slug)
        
    else:
        goods = Products.objects.all()

    context: dict[str, Any] = {
        "title": "Sweet Point - Каталог",
        "goods": goods
    }
    return render(request, "goods/catalog.html", context)


# может добавлю отзывы
