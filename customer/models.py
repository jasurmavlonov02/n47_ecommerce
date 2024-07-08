from datetime import datetime, timezone

from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import PermissionsMixin

from django.db import models

from customer.managers import CustomUserManager


# Create your models here.


class Customer(models.Model):
    full_name = models.CharField(max_length=155, null=True, blank=True)  # verbose_name="To'liq ismi")
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=20)
    address = models.CharField(max_length=150)
    joined = models.DateTimeField(default=datetime.now())
    image = models.ImageField(upload_to='customer/', null=True, blank=True)
    is_active = models.BooleanField(default=False)

    def __str__(self):
        return self.email

    class Meta:
        ordering = ('-joined',)
        verbose_name_plural = 'Customers'
        # verbose_name = 'Xaridor'


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=255, null=True, blank=True)
    birth_of_date = models.DateField(null=True, blank=True)

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=True)

    objects = CustomUserManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email

    def save(self, *args, **kwargs):
        if self.password and not self.password.startswith(('pbkdf2_sha256$', 'bcrypt$', 'argon2')):
            self.password = make_password(self.password)

        super().save(*args, **kwargs)
