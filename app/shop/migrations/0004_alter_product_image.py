# Generated by Django 3.2.4 on 2021-06-16 13:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_alter_product_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(upload_to='products', verbose_name='Изображение'),
        ),
    ]
