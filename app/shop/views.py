from rest_framework import generics

from app.shop.models import Category, Product
from app.shop.pagination import ProductsPagination
from app.shop.serializer import ProductSerializer, CategorySerializer


class GetListAllCategory(generics.ListAPIView):
    serializer_class = CategorySerializer

    def get_queryset(self):
        return Category.objects.all()


class GetListAllProduct(generics.ListAPIView):
    serializer_class = ProductSerializer
    pagination_class = ProductsPagination

    def get_queryset(self):
        return Product.objects.all()
