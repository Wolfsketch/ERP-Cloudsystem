# Generated by Django 5.0.6 on 2024-05-30 19:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ERPWinkel', '0002_alter_categorie_options_product_is_sale_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='is_Sale',
            new_name='Korting',
        ),
    ]
