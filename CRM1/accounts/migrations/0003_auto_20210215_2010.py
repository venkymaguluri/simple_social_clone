# Generated by Django 3.1.4 on 2021-02-15 14:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_orders_products'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Orders',
            new_name='Order',
        ),
        migrations.RenameModel(
            old_name='Products',
            new_name='Product',
        ),
    ]
