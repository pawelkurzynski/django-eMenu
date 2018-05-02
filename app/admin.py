from django.contrib import admin

from .models import *
# Register your models here.

class MenuAdmin(admin.ModelAdmin):
    fields = ['title','text', 'pub_date', 'mod_date']
    list_display = ('title', 'pub_date', 'mod_date')
    list_filter = ['pub_date', 'mod_date']
    search_fields = ['title']
 


class DishAdmin(admin.ModelAdmin):
    fields = ['name','text','price','makingtime',' vegetarian','icon', 'pub_date', 'menus']
    list_display = ('name', 'pub_date')
    list_filter = ['pub_date']
    search_fields = ['name']


admin.site.register(Menu, MenuAdmin)
admin.site.register(Dish, DishAdmin)