# Generated by Django 4.1.7 on 2023-04-17 04:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product_app', '0013_remove_cartitem_image_cartitem_image_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cartitem',
            name='image_url',
            field=models.ImageField(blank=True, default=4, upload_to='product/images'),
            preserve_default=False,
        ),
    ]
