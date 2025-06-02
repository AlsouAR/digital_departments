from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator


class User(AbstractUser):
    image = models.ImageField(upload_to='users_images', blank=True,null=True, verbose_name='Аватар')
    phone = models.CharField(max_length=20,blank=True,null=True, verbose_name='Номер телефона',
        validators=[
            RegexValidator(regex=r'^\+?1?\d{9,15}$',
                message="формат: '+79991234567' "
            )
        ]
    )
    address = models.CharField(max_length=255, blank=True, null=True, verbose_name='Адрес')
    class Meta:
        db_table = 'user'
        verbose_name='Пользователя'
        verbose_name_plural='Пользователи'
    
    def __str__(self):
        return self.username
