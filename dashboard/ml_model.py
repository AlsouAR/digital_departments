# dashboard/ml_model.py
from orders.models import OrderItem
import pandas as pd
from sklearn.linear_model import LinearRegression
from collections import defaultdict


def get_dashboard_data():
    items = OrderItem.objects.all().select_related('product__category')

    if not items.exists():
        return {
            'total_orders': 0,
            'total_revenue': 0,
            'top_products': [],
            'top_categories': [],
            'price_recommendations': [],
            'forecast': {}
        }

    # Подсчёт метрик
    total_orders = items.values('order').distinct().count()
    total_products_sold = sum(item.quantity for item in items)
    total_revenue = sum(item.products_price() for item in items)

    # ТОП-товары
    product_sales = defaultdict(int)
    for item in items:
        product_sales[item.product.name] += item.quantity
    top_products = sorted(product_sales.items(), key=lambda x: x[1], reverse=True)[:4]

    # ТОП-категории
    category_sales = defaultdict(int)
    for item in items:
        category_sales[item.product.category.name] += item.quantity
    top_categories = sorted(category_sales.items(), key=lambda x: x[1], reverse=True)

    # Прогноз спроса по категориям
    df = pd.DataFrame(list(items.values()))
    df['created_timestamp'] = pd.to_datetime(df['created_timestamp'])
    df['month'] = df['created_timestamp'].dt.month

    def train_predict(data):
        X = data[['month']]
        y = data['quantity']
        model = LinearRegression()
        model.fit(X, y)
        future_months = [[m] for m in range(1, 13)]
        return model.predict(future_months).astype(int).tolist()

    forecast_by_category = {}
    for _, row in df.iterrows():
        cat_name = items.get(id=row['id']).product.category.name
        if cat_name not in forecast_by_category:
            forecast_by_category[cat_name] = []
        forecast_by_category[cat_name].append(row)

    category_forecasts = {}
    for cat, rows in forecast_by_category.items():
        data = pd.DataFrame(rows)
        category_forecasts[cat] = train_predict(data)

    # Рекомендации по цене
    price_recommendations = []
    if len(top_products) >= 2:
        high_demand_product = top_products[0][0]
        low_demand_product = top_products[-1][0]
        price_recommendations.append({
            'name': high_demand_product,
            'action': 'Повысьте цену',
            'reason': '+10% — высокий спрос'
        })
        price_recommendations.append({
            'name': low_demand_product,
            'action': 'Снизьте цену',
            'reason': '-15% — низкий спрос'
        })

    return {
        'total_orders': total_orders,
        'total_revenue': round(total_revenue, 2),
        'total_products_sold': total_products_sold,
        'top_products': top_products,
        'top_categories': top_categories,
        'price_recommendations': price_recommendations,
        'forecast': category_forecasts
    }