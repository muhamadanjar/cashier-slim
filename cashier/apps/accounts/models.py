from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    class RoleChoices(models.TextChoices):
        ADMIN = 'ADMIN'
        USER = 'USER'
        MANAGER = 'MANAGER'
        CUSTOMER = 'CUSTOMER'
    role = models.CharField(max_length=10, default=RoleChoices.USER, choices=RoleChoices.choices)


class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.email


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=20, null=True, blank=True)
    address = models.CharField(max_length=255, null=True, blank=True)
    city = models.CharField(max_length=255, null=True, blank=True)
    state = models.CharField(max_length=255, null=True, blank=True)
    zip = models.CharField(max_length=5, null=True, blank=True)
    country = models.CharField(max_length=255, null=True, blank=True)
    picture = models.ImageField(upload_to='profile/', blank=True)

    def __str__(self):
        return self.user.username
