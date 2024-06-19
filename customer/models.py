from datetime import datetime, timezone

from django.db import models


# Create your models here.


class Customer(models.Model):
    full_name = models.CharField(max_length=155, null=True, blank=True)  # verbose_name="To'liq ismi")
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=20)
    address = models.CharField(max_length=150)
    joined = models.DateTimeField(default=datetime.now())
    image = models.ImageField(upload_to='customer/', null=True, blank=True)

    def __str__(self):
        return self.email

    class Meta:
        ordering = ('-joined',)
        verbose_name_plural = 'Customers'
        # verbose_name = 'Xaridor'
