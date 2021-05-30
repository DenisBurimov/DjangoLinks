from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('home', views.home, name='home'),
    path('links', views.links, name='links'),
    path('add', views.add, name='add'),
    path('about', views.about, name='about')
]