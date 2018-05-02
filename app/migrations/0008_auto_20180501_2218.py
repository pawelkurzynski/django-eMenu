# Generated by Django 2.0.4 on 2018-05-01 21:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_auto_20180429_1810'),
    ]

    operations = [
        migrations.AddField(
            model_name='dish',
            name='vegetarian',
            field=models.BooleanField(default=False, verbose_name='Wegetarianskie'),
        ),
        migrations.AlterField(
            model_name='dish',
            name='makingtime',
            field=models.PositiveIntegerField(default=0, verbose_name='Czas przygotowanie'),
        ),
        migrations.AlterField(
            model_name='dish',
            name='price',
            field=models.PositiveIntegerField(default=0, verbose_name='Cena'),
        ),
    ]
