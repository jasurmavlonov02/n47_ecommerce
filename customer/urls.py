from django.urls import path

from customer.views.auth import login_page, logout_page, register_page, LoginPageView, LoginPage, RegisterFormView
from customer.views.customers import customers, add_customer, delete_customer, edit_customer, export_data

urlpatterns = [
    path('customer-list/', customers, name='customers'),
    path('add-customer/', add_customer, name='add_customer'),
    path('customer/<int:pk>/delete', delete_customer, name='delete'),
    path('customer/<int:pk>/update', edit_customer, name='edit'),
    # Authentication path
    path('login-page/', LoginPage.as_view(), name='login'),
    path('logout-page/', logout_page, name='logout'),
    path('register-page/', RegisterFormView.as_view(), name='register'),
    path('export-data/', export_data, name='export_data')
]
