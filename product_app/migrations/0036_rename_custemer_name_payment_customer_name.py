# Generated by Django 4.2 on 2023-05-03 19:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product_app', '0035_payment'),
    ]

    operations = [
        migrations.RenameField(
            model_name='payment',
            old_name='custemer_name',
            new_name='customer_name',
        ),
    ]
