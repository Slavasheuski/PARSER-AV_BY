# Generated by Django 4.1.7 on 2023-03-24 12:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('av', '0004_alter_product_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.IntegerField(verbose_name='Цена, $'),
        ),
    ]
