from django.db import models
from pytz import unicode


class Slider(models.Model):
    image = models.ImageField(upload_to='main_sliders', verbose_name="Изображение")
    title = models.CharField(max_length=120, verbose_name='Заголовок')
    body = models.TextField(verbose_name='Описание')
    alt = models.TextField(verbose_name='Подсказка пользователю')


    class Meta:
        verbose_name = 'Картинка для главного экрана'
        verbose_name_plural = 'Картинки для главного экрана'

    def __str__(self):
        return unicode(str(self.title))