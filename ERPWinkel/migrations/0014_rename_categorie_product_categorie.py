# Generated by Django 5.0.6 on 2024-06-01 11:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ERPWinkel', '0013_alter_product_categorie'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='categorie',
            new_name='Categorie',
        ),
    ]
