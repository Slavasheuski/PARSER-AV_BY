# Generated by Django 4.1.7 on 2023-03-24 06:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('av', '0002_alter_product_options_product_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='url',
            field=models.TextField(default='None', unique=True, verbose_name='URL адрес объявления'),
        ),
    ]
