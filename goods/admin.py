from django.contrib import admin

# Register your models here.
from goods.models import Categories, Products

# admin.site.register(Categories)  # для создания таблицы на типосервере
# admin.site.register(Products)

@admin.register(Categories) # тонкая настройка
class CategoriesAdmin(admin.ModelAdmin):
    prepopulated_fields={'slug': ('name',)}

@admin.register(Products) # тонкая настройка
class ProductsAdmin(admin.ModelAdmin):
    prepopulated_fields={'slug': ('name',)}

