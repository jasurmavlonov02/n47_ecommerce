from django.urls import path

from customer.views.auth import login_page, logout_page, register_page, LoginPageView, LoginPage, RegisterFormView, \
    verify_email_confirm, verify_email_done
from customer.views.customers import customers, add_customer, delete_customer, edit_customer, export_data, share_mail

urlpatterns = [
    path('customer-list/', customers, name='customers'),
    path('add-customer/', add_customer, name='add_customer'),
    path('customer/<int:pk>/delete', delete_customer, name='delete'),
    path('customer/<int:pk>/update', edit_customer, name='edit'),
    # Authentication path
    path('login-page/', LoginPage.as_view(), name='login'),
    path('logout-page/', logout_page, name='logout'),
    path('register-page/', register_page, name='register'),
    path('export-data/', export_data, name='export_data'),
    path('sending-mail/', share_mail, name='share_mail'),
    # sending
    path('verify-email-done/', verify_email_done, name='verify_email_done'),
    path('verify-email-confirm/<uidb64>/<token>/', verify_email_confirm, name='verify_email_confirm'),
]
