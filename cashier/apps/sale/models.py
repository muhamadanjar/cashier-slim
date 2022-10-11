from django.db import models

from cashier.apps import accounts
from djmoney.models.fields import MoneyField
from djmoney.money import Money


class Order(models.Model):
    """
    Order model
    """
    STATUS_CHOICES = (
        ('pending', 'Pending'),
        ('paid', 'Paid'),
        ('cancelled', 'Cancelled'),
    )
    name = models.CharField(max_length=255)
    code = models.CharField(max_length=100)
    references = models.CharField(max_length=50, null=True, blank=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending')
    amount_tax = MoneyField(max_digits=10, decimal_places=2, default=0.00)
    amount_price = MoneyField(max_digits=10, decimal_places=2)
    amount_change = MoneyField(max_digits=10, decimal_places=2)
    amount_payment = MoneyField(max_digits=10, decimal_places=2)
    order_date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey('accounts.User', on_delete=models.CASCADE, related_name='user')
    customer = models.ForeignKey('accounts.Customer', on_delete=models.CASCADE, null=True, blank=True,
                                 related_name='customer')
    notes = models.CharField(max_length=255, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    order_lines = models.ManyToManyField("sale.OrderItem",
                                         related_name='lines')

    def __str__(self):
        return str(self.id)


class OrderItem(models.Model):
    """
    Order item model
    """
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')
    item = models.ForeignKey('product.Item', on_delete=models.CASCADE, related_name='product_item')
    quantity = models.IntegerField(default=1)
    subtotal = MoneyField(max_digits=10, decimal_places=2, null=True)

    def __str__(self):
        return str(self.order.name)

