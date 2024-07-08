from django.contrib import admin

from customer.forms import UserModelForm
from customer.models import Customer, User


# Register your models here.
# admin.site.register(Customer)


@admin.register(Customer)
class CustomerModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'full_name', 'email', 'is_active']
    search_fields = ['email', 'id']
    list_filter = ['joined', 'is_active']


@admin.register(User)
class UserModelAdmin(admin.ModelAdmin):
    list_display = ['email', 'username', 'birth_of_date', 'is_superuser']
    form = UserModelForm



