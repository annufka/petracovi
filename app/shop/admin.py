from django.contrib import admin

from app.shop.models import Category, Product


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'slug', 'price')

admin.site.register(Category)
admin.site.register(Product, ProductAdmin)