
from rest_framework import serializers
from .models import *


class MenuSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Menu
        fields = ('id', 'title', 'text', 'pub_date', 'mod_date')


class DishSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Dish
        fields = ('id', 'name', 'text', 'price', 'makingtime', 'pub_date', 'vegetarian', 'icon')