# digital_departments
Веб-платформа для интернет-магазина кондитерской с функциями анализа данных и прогнозирования спроса

## Запуск приложения для разработки
- `python -m venv venv` - создание виртуального окружения
- `venv\Scripts\activate` - войти в виртуальное окружение
- `pip install -r requirements` - установка зависимостей
- `python manage.py runserver` или `Ctrl+F5` - запустить сервер для разработки на http://127.0.0.1:8000
- `pip install -r requirements.txt` - установка зависимостей

- `python manage.py makemigrations` - загрузка моделей
- `python manage.py migrate` - применение миграций(создание бд)

- `python manage.py createsuperuser` - создание суперпользователя для джанго

- `python manage.py loaddata fixtures/goods/categories.json` - загрузка фикстур категории
- `python manage.py loaddata fixtures/goods/products.json` - загрузка фикстур продуктов
