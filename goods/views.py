from typing import Any
from unicodedata import category
from django.shortcuts import render
from django.http import HttpResponse

from goods.models import Products


def catalog(request, category_slug=None):

    on_sale = request.GET.get('on_sale', None)
    order_by = request.GET.get('order_by', None)

    if category_slug and category_slug != 'all':
        goods = Products.objects.filter(category__slug=category_slug)
    else:
        goods = Products.objects.all()

    if on_sale:
        goods = goods.filter(discount__gt=0)
    
    if order_by and order_by!='default':
        goods = goods.order_by(order_by)

    context: dict[str, Any] = {
        "title": "Sweet Point - Каталог",
        "goods": goods,
        "slug_url": category_slug
    }
    return render(request, "goods/catalog.html", context)


# может добавлю отзывы
