# Generated by Django 2.0.4 on 2018-04-29 17:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_dish_icon'),
    ]

    operations = [
        migrations.AddField(
            model_name='dish',
            name='makingtime',
            field=models.IntegerField(default=0, verbose_name='Czas przygotowanie'),
        ),
        migrations.AlterField(
            model_name='dish',
            name='price',
            field=models.IntegerField(default=0, verbose_name='Cena'),
        ),
    ]