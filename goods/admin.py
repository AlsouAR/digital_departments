from django.contrib import admin

# Register your models here.
from goods.models import Categories, Products

# admin.site.register(Categories)  # для создания таблицы на типосервере
# admin.site.register(Products)

@admin.register(Categories) # тонкая настройка
class CategoriesAdmin(admin.ModelAdmin):
    prepopulated_fields={'slug': ('name',)}
    list_display = ["name",]

@admin.register(Products) # тонкая настройка
class ProductsAdmin(admin.ModelAdmin):
    prepopulated_fields={'slug': ('name',)}
    list_display = ["name", "rating", "price", "discount"]
    list_editable = ["discount",]
    search_fields = ["name", "rating"]
    list_filter = ["discount", "rating", "category"]
    fields = [
        "name",
        "category",
        "slug",
        "rating",
        "image",
        ("price", "discount"),
    ]
