# Generated by Django 4.1.2 on 2022-10-11 06:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sale', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='order_lines',
            field=models.ManyToManyField(blank=True, null=True, related_name='lines', to='sale.orderitem'),
        ),
    ]