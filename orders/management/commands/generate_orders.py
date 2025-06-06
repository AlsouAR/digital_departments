from django.core.management.base import BaseCommand
from goods.models import Products
from orders.models import OrderItem
import csv
from datetime import datetime


class Command(BaseCommand):
    help = 'Генерация заказов из CSV'

    def add_arguments(self, parser):
        parser.add_argument('file_path', type=str, help='Путь к CSV-файлу')

    def handle(self, *args, **kwargs):
        file_path = kwargs['file_path']

        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                reader = csv.DictReader(f)
                for row in reader:
                    product_id = int(row['product_id'])
                    product_name = row['product_name']
                    quantity = int(row['quantity'])
                    created = row['created_timestamp']

                    try:
                        product = Products.objects.get(id=product_id)
                        if product.name != product_name:
                            self.stdout.write(self.style.WARNING(
                                f'⚠️ Название товара "{product_name}" не совпадает с базой "{product.name}"'))
                    except Products.DoesNotExist:
                        self.stdout.write(self.style.WARNING(
                            f'⚠️ Товар "{product_name}" не найден в базе'))
                        continue

                    OrderItem.objects.create(
                        order=None,
                        product=product,
                        name=product.name,
                        price=product.display_new_price(),
                        quantity=quantity,
                        created_timestamp=datetime.strptime(created, '%Y-%m-%d')
                    )

                    self.stdout.write(self.style.SUCCESS(
                        f'✅ Добавлено: {product.name} × {quantity} шт.'
                    ))

                self.stdout.write(self.style.SUCCESS('🎉 Импорт завершён'))

        except FileNotFoundError:
            self.stdout.write(self.style.ERROR('❌ Файл не найден'))