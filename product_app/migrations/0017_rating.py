# Generated by Django 4.1.7 on 2023-04-17 09:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product_app', '0016_remove_billingaddress_user_delete_cartitem_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('one', models.PositiveIntegerField(blank=True, default=0, null=True)),
                ('two', models.PositiveIntegerField(blank=True, default=0, null=True)),
                ('three', models.PositiveIntegerField(blank=True, default=0, null=True)),
                ('four', models.PositiveIntegerField(blank=True, default=0, null=True)),
                ('five', models.PositiveIntegerField(blank=True, default=0, null=True)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rating', to='product_app.product')),
            ],
            options={
                'ordering': ['product'],
            },
        ),
    ]