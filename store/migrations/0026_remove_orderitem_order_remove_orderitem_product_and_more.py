# Generated by Django 4.1.5 on 2023-04-25 16:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0025_orderitem'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orderitem',
            name='order',
        ),
        migrations.RemoveField(
            model_name='orderitem',
            name='product',
        ),
        migrations.DeleteModel(
            name='Order',
        ),
        migrations.DeleteModel(
            name='OrderItem',
        ),
    ]