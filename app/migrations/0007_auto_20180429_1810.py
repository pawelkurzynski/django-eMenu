# Generated by Django 2.0.4 on 2018-04-29 17:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_auto_20180429_1810'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menu',
            name='mod_date',
            field=models.DateTimeField(verbose_name='Data aktualizacji'),
        ),
        migrations.AlterField(
            model_name='menu',
            name='pub_date',
            field=models.DateTimeField(verbose_name='Data dodania'),
        ),
    ]
