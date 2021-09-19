from django.urls import path

from app.shop.views import GetListAllCategory, GetListAllProduct

urlpatterns = [
    path('get/all/categories/', GetListAllCategory.as_view()),
    path('get/all/products/', GetListAllProduct.as_view()),
]