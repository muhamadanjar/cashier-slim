from django.db import models

from cashier.apps import accounts


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
    amount_tax = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    amount_price = models.DecimalField(max_digits=10, decimal_places=2)
    amount_change = models.DecimalField(max_digits=10, decimal_places=2)
    amount_payment = models.DecimalField(max_digits=10, decimal_places=2)
    order_date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey('accounts.User', on_delete=models.CASCADE)
    customer = models.ForeignKey('accounts.Customer', on_delete=models.CASCADE, null=True, blank=True)
    notes = models.CharField(max_length=255, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.id)


class OrderItem(models.Model):
    """
    Order item model
    """
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    item = models.ForeignKey('product.Item', on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    subtotal = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return str(self.order.name)

