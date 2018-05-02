import datetime

from django.db import models
from django.utils import timezone

# Create your models here.

class Menu(models.Model):
    title = models.CharField('Tytuł karty menu', unique=True, max_length=100)
    text = models.TextField(verbose_name='Opis')
    pub_date = models.DateTimeField('Data dodania')
    mod_date = models.DateTimeField('Data aktualizacji')

    class Meta:
        verbose_name = "Karta"
        verbose_name_plural = "Karty"

    def __str__(self):
        return self.title


class Dish(models.Model): 
    name = models.CharField('Nazwa dania', max_length=255)
    text = models.TextField(verbose_name='Opis')
    price = models.PositiveIntegerField('Cena', default=0)
    makingtime = models.PositiveIntegerField('Czas przygotowanie', default=0)
    menus = models.ManyToManyField(Menu, verbose_name='Karta') 
    pub_date = models.DateTimeField('Data dodania')
    vegetarian = models.BooleanField('Wegetarianskie', default=False)
    icon = models.ImageField('Ikonka Dania', upload_to='icons',
                              blank=True)

    class Meta:
        verbose_name = "Danie"
        verbose_name_plural = "Dania"

    def __str__(self):
        return self.name