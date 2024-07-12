from django.contrib import admin
from django.urls import path, include
from app.views import (
    ProductListView,
    ProductDetailTemplateView,
    AddProductView,
    EditProductView,
    ProductDeleteView,
    EditProductTemplateView
)

urlpatterns = [
    path('index/', ProductListView.as_view(), name='index'),
    path('product-detail/<int:product_id>', ProductDetailTemplateView.as_view(), name='product_detail'),

    path('add-product/', AddProductView.as_view(), name='add_product'),
    path('update-product/<int:pk>/', EditProductTemplateView.as_view(), name='update_product'),
    path('delete-product/<int:pk>/', ProductDeleteView.as_view(), name='product_delete')
]
