# Generated by Django 4.1.2 on 2022-10-11 06:44

from django.db import migrations, models
import djmoney.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('sale', '0002_order_order_lines'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='order_lines',
            field=models.ManyToManyField(related_name='lines', to='sale.orderitem'),
        ),
        migrations.AlterField(
            model_name='orderitem',
            name='subtotal',
            field=djmoney.models.fields.MoneyField(decimal_places=2, max_digits=10, null=True),
        ),
    ]
