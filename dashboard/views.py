# dashboard/views.py
from django.shortcuts import render
from .ml_model import get_dashboard_data
from datetime import datetime


# def dashboard(request):
#     data = get_dashboard_data()
    
#     context = {
#         'total_orders': data['total_orders'],
#         'total_revenue': data['total_revenue'],
#         'total_products_sold': data['total_products_sold'],
#         'top_products': data['top_products'],
#         'top_categories': data['top_categories'],
#         'recommendations': data['price_recommendations'],
#         'forecast': data['forecast'],
#     }

#     return render(request, 'dashboard/dashboard.html', context)

def dashboard(request):
    data = get_dashboard_data()

    # Генерируем названия месяцев начиная с текущего
    current_month = datetime.now().month
    months = ['Янв', 'Фев', 'Мар', 'Апр', 'Май', 'Июн',
              'Июл', 'Авг', 'Сен', 'Окт', 'Ноя', 'Дек']

    forecast_labels = []
    for i in range(12):
        idx = (current_month + i - 1) % 12
        forecast_labels.append(months[idx])

    context = {
        'total_orders': data['total_orders'],
        'total_revenue': round(data['total_revenue'], 2),
        'total_products_sold': data['total_products_sold'],
        'top_products': data['top_products'],
        'top_categories': data['top_categories'],
        'recommendations': data['price_recommendations'],
        'forecast': data['forecast'],
        'forecast_labels': forecast_labels  # передаем в шаблон
    }

    return render(request, 'dashboard/dashboard.html', context)
