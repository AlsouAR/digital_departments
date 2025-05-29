from typing import Any
from django.shortcuts import render
from django.http import HttpResponse


def catalog(request):
    context: dict[str, Any] = {
        "title": "Sweet Point - Каталог",
        "goods": [
            {
                "name": "Торт Клубничный",
                "price": 1200,
                "image": "deps/images/product-cake.jpg",
                "category": "cakes",
                "rating": 4.8,
                "badges": [],
            },
            {
                "name": "Торт Шоколадный",
                "price": 1100,
                "image": "deps/images/product-chocolate-cake.jpg",
                "category": "cakes",
                "rating": 4.9,
                "badges": ["new"],
            },
            {
                "name": "Эклеры шоколадные",
                "price": 350,
                "image": "deps/images/product-eclair.jpg",
                "category": "desserts",
                "rating": 4.7,
                "badges": [],
            },
            {
                "name": "Макаруны ассорти",
                "price": 380,
                "old_price": 450,  # Старая цена для акции
                "image": "deps/images/product-macarons.jpg",
                "category": "desserts",
                "rating": 4.8,
                "badges": ["discount"],
                "discount": 15,
            },
            {
                "name": "Круассан классический",
                "price": 180,
                "image": "deps/images/product-croissant.jpg",
                "category": "pastry",
                "rating": 4.9,
                "badges": ["new"],
            },
            {
                "name": "Булочка с корицей",
                "price": 150,
                "image": "deps/images/product-cinnamon-roll.jpg",
                "category": "pastry",
                "rating": 4.7,
                "badges": [],
            },
            {
                "name": "Пирог с яблоками",
                "price": 550,
                "old_price": 650,  # Старая цена для акции
                "image": "deps/images/product-pie.jpg",
                "category": "pies",
                "rating": 4.6,
                "badges": ["discount"],
                "discount": 15,
            },
            {
                "name": "Пирог с вишней",
                "price": 600,
                "image": "deps/images/product-cherry-pie.jpg",
                "category": "pies",
                "rating": 4.5,
                "badges": [],
            },
        ],
    }
    return render(request, "goods/catalog.html", context)


# может добавлю отзывы
