from django.contrib import admin
from django.contrib.auth.models import User, Group

from app.models import Product, Image, Attribute, AttributeValue, ProductAttribute
from customer.models import User

# Register your models here.


# admin.site.register(Product)
admin.site.register(Image)
admin.site.register(Attribute)
admin.site.register(AttributeValue)
admin.site.register(ProductAttribute)


# admin.site.unregister(User)
# admin.site.unregister(Group)
# admin.site.register(User)

class ProductModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'discount', 'price')
    search_fields = ('name',)
    list_per_page = 2


admin.site.register(Product, ProductModelAdmin)
