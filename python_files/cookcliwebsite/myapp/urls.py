from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('recipes/', views.recipes, name='recipes'),
    path('shopping-list/', views.shopping_list, name='shopping_list'),
]

