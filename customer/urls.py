from django.urls import path

from customer.views.auth import login_page
from customer.views.customers import customers, add_customer, delete_customer, edit_customer

urlpatterns = [
    path('customer-list/', customers, name='customers'),
    path('add-customer/', add_customer, name='add_customer'),
    path('customer/<int:pk>/delete', delete_customer, name='delete'),
    path('customer/<int:pk>/update', edit_customer, name='edit'),
    # Authentication path
    path('login-page/', login_page, name='login')
]
