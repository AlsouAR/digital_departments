from tabnanny import verbose
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.
class Categories(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name='Название')
    slug = models.SlugField(max_length=200, unique=True, blank=True, null=True, verbose_name='URL')

    class Meta:
        db_table = 'category'
        verbose_name='Категорию'
        verbose_name_plural='Категории'
    
    def __str__(self):
        return self.name

class Products(models.Model):
    name = models.CharField(max_length=200, unique=True, verbose_name='Название')
    slug = models.SlugField(max_length=200, unique=True, blank=True, null=True, verbose_name='URL')
    image = models.ImageField(upload_to='goods_imagies', blank=True, null=True, verbose_name='Изображение')
    price = models.DecimalField(default=0.00, max_digits=10, decimal_places=2, verbose_name='Цена')
    discount = models.DecimalField(default=0.00, max_digits=10, decimal_places=2, verbose_name='Скидка в %')
    category = models.ForeignKey(to=Categories, on_delete=models.CASCADE, verbose_name='Категория')
    rating = models.FloatField(default=0.0, validators=[MinValueValidator(1), MaxValueValidator(5)], 
                                         blank=True, null=True, verbose_name='Оценка')
    
    class Meta:
        db_table = 'product'
        verbose_name='Продукт'
        verbose_name_plural='Продукты'
        
    def __str__(self):
        return self.name
    
    def display_new_price(self):
        if self.discount:
            new_price = self.price - self.price*(self.discount/100)
            return int(new_price)
        return int(self.price)
    
    def display_discount(self):
        return int(self.discount)
    