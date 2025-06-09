from django import template
from dashboard.ml_model import get_dashboard_data
from goods.models import Products
from django.core.cache import cache
from django.utils import timezone
from datetime import timedelta

register = template.Library()


@register.simple_tag()
def tag_dashboard():
    cache_key = "dashboard_data_enriched"
    cached_data = cache.get(cache_key)

    if cached_data is not None:
        return cached_data
    # Получаем данные из ML-модели
    dashboard_data = get_dashboard_data()

    # Получаем все товары и строим словарь {name: product}
    all_products = Products.objects.all()
    product_dict = {product.name: product for product in all_products}

    # Обогащаем top_products данными из модели Product
    enriched_top_products = []

    for product_name, sales_count in dashboard_data['top_products']:
        if product_name in product_dict:
            product = product_dict[product_name]
            enriched_top_products.append({
                'name': product.name,
                'price': product.price,
                'discount': product.discount,
                'rating': product.rating,
                'image_url': product.image.url if product.image else None,
                'id': product.id,
                'display_new_price': product.display_new_price,  # если есть такой метод/свойство
                'display_discount': product.display_discount,    # если есть такое свойство
            })

    # Заменяем "голые" названия на обогащённые данные
    dashboard_data['top_products'] = enriched_top_products
    # Сохраняем в кэш на 5 минут
    cache.set(cache_key, dashboard_data, 60 * 5)

    return dashboard_data