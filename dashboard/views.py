# dashboard/views.py
from django.shortcuts import render
from .ml_model import get_dashboard_data


def dashboard(request):
    data = get_dashboard_data()
    
    context = {
        'total_orders': data['total_orders'],
        'total_revenue': data['total_revenue'],
        'total_products_sold': data['total_products_sold'],
        'top_products': data['top_products'],
        'top_categories': data['top_categories'],
        'recommendations': data['price_recommendations'],
        'forecast': data['forecast'],
    }

    return render(request, 'dashboard/dashboard.html', context)