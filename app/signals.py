import os
import json
from django.db.models.signals import pre_save, post_save, pre_delete
from config.settings import BASE_DIR
from app.models import Product
from django.dispatch import receiver


@receiver(post_save, sender=Product)
def product_save(sender, instance, created, **kwargs):
    if created:
        print(f'{instance.name} is created!')
        print(kwargs)
    else:
        print('Product Updated')


@receiver(pre_delete, sender=Product)
def product_delete(sender, instance, **kwargs):
    file_path = os.path.join(BASE_DIR,'app/delete_products/', f'product_{instance.id}.json')

    product_data = {
        'id': instance.id,
        'name': instance.name,
        'price': instance.price,
        'description': instance.description
    }

    with open(file_path, mode='w') as file_json:
        json.dump(product_data, file_json, indent=4)

    print(f'{instance.name} is deleted')
