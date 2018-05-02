
# Create your views here.

from django.views import generic
from .models import *
from django.db.models import Count
from rest_framework import viewsets
from .serializers import *


class IndexView(generic.ListView):
    template_name = 'app/index_list.html'
    context_object_name = 'latest_menu_list'
    paginate_by = 10

    def get_queryset(self):
     
        return Menu.objects.exclude(dish__menus__isnull=True).order_by('id')
     
        
class DetailView(generic.DetailView):
    model = Menu
    template_name = 'app/detail.html'
    

class NameIndexView(IndexView):
    template_name = 'app/index_list.html'

    def get_queryset(self):
     
        return Menu.objects.exclude(dish__menus__isnull=True).order_by('title')
        

class NumberDishesIndexView(IndexView):
    template_name = 'app/index_list.html'

    def get_queryset(self):
        return Menu.objects.exclude(dish__menus__isnull=True).annotate(dishes=Count('dish')).order_by('-dishes')
      

class MenuViewSet(viewsets.ModelViewSet):
    
    queryset = Menu.objects.exclude(dish__menus__isnull=True).order_by('title')
                                                            
    serializer_class = MenuSerializer
    http_method_names = ['get']
     
        
class DishViewSet(viewsets.ModelViewSet):
    queryset = Dish.objects.all()
    serializer_class = DishSerializer
    http_method_names = ['get']
  
class List(generic.ListView):
    template_name = 'app/index_list.html'
    context_object_name = 'latest_menu_list'
    def get_queryset(self):
     
       return Menu.objects.exclude(dish__menus__isnull=True).order_by('id')