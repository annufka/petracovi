from django.contrib.auth.models import User
from django.contrib.contenttypes.models import ContentType
from django.db import models
from pytz import unicode


class Category(models.Model):
    name = models.CharField(max_length=255, verbose_name='Имя категории')
    slug = models.SlugField(unique=True, verbose_name='Название категории для адресной строки')

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return unicode(str(self.name))


class Product(models.Model):
    category = models.ForeignKey(Category, verbose_name="Категория", on_delete=models.CASCADE)
    name = models.CharField(max_length=255, verbose_name='Наименование')
    slug = models.SlugField(unique=True, verbose_name='Название товара для адресной строки')
    image = models.ImageField(upload_to='products', verbose_name="Изображение")
    description = models.TextField(verbose_name="Описание", null=True)
    price = models.DecimalField(max_digits=9, decimal_places=2, verbose_name="Цена")

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

    def __str__(self):
        return unicode(str(self.name))
