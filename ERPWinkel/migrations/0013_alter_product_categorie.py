# Generated by Django 5.0.6 on 2024-06-01 11:42

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ERPWinkel', '0012_alter_categorie_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='categorie',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ERPWinkel.categorie'),
        ),
    ]