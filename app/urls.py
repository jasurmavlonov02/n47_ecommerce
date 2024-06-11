from django.contrib import admin
from django.urls import path, include
from app.views import index, product_detail

urlpatterns = [
    path('index/', index, name='index'),
    path('product-detail/<int:product_id>', product_detail, name='product_detail')
]
