# Generated by Django 4.1.5 on 2023-04-20 08:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0021_order_orderitem'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='cart_total_price',
        ),
    ]