# Generated by Django 3.2.4 on 2021-06-16 13:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(upload_to='media', verbose_name='Изображение'),
        ),
    ]
