# Generated by Django 4.2 on 2023-04-13 04:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product_app', '0008_cartitem_image_cartitem_size'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cartitem',
            old_name='image',
            new_name='Image',
        ),
        migrations.RenameField(
            model_name='cartitem',
            old_name='product_price',
            new_name='price',
        ),
    ]