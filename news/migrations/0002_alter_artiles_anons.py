# Generated by Django 4.1.7 on 2023-04-07 12:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='artiles',
            name='anons',
            field=models.CharField(default='None', max_length=250, unique=True, verbose_name='Анонс'),
        ),
    ]
