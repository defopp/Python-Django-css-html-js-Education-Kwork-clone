# Generated by Django 5.0.2 on 2024-05-07 10:21

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('messageApp', '0001_initial'),
        ('productsApp', '0005_product_main_cat_product_sub_cat'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chatroom',
            name='product',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='product', to='productsApp.product'),
        ),
    ]
