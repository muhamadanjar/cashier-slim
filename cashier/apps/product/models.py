from django.db import models
from djmoney.models.fields import MoneyField

from cashier.apps import accounts


class Item(models.Model):
    name = models.CharField(max_length=255)
    code = models.CharField(max_length=100)
    stock = models.IntegerField(default=0)
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    description = models.TextField(blank=True)
    price = MoneyField(max_digits=10, decimal_places=2)
    sell = MoneyField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='images/', blank=True)
    user_id = models.ForeignKey('accounts.User', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Attribute(models.Model):
    name = models.CharField(max_length=255)
    display_order = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class AttributeValue(models.Model):
    attribute = models.ForeignKey(Attribute, on_delete=models.CASCADE, related_name='attribute_value')
    name = models.CharField(max_length=255)
    product = models.ForeignKey(Item, related_name='product', null=True, blank=True, on_delete=models.CASCADE)
    display_order = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
