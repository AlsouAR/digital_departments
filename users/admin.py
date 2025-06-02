from django.contrib import admin

# Register your models here.
from users.models import User

admin.site.register(User)  # для создания таблицы на типосервере
