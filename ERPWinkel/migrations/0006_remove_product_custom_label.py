# Generated by Django 5.0.6 on 2024-05-31 11:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ERPWinkel', '0005_product_custom_label_alter_product_korting_prijs'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='custom_label',
        ),
    ]
