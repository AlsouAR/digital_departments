from typing import Any
from django.shortcuts import render
from django.http import HttpResponse

from goods.models import Products


def catalog(request):

    goods = Products.objects.all()

    context: dict[str, Any] = {
        "title": "Sweet Point - Каталог",
        "goods": goods
    }
    return render(request, "goods/catalog.html", context)


# может добавлю отзывы
