# Generated by Django 2.0.4 on 2018-04-29 14:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_auto_20180429_1447'),
    ]

    operations = [
        migrations.AddField(
            model_name='dish',
            name='icon',
            field=models.ImageField(blank=True, upload_to='icons', verbose_name='Ikonka Dania'),
        ),
    ]
