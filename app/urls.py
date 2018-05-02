
from django.urls import path
from django.conf.urls import url, include
from rest_framework import routers

from . import views

router = routers.DefaultRouter()
router.register(r'menus', views.MenuViewSet)
router.register(r'dishes', views.DishViewSet)

app_name = 'app'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index_list'),
    path('sortbyname/', views.NameIndexView.as_view(), name='index_sortbyname'),
    path('sortbydishnumber/', views.NumberDishesIndexView.as_view(), name='index_sortbynumber'),
    path('menu/<int:pk>', views.DetailView.as_view(), name='detail'),
    url(r'^api', include(router.urls)),
    path('menuapi', views.List.as_view(), name='index_api'),
]