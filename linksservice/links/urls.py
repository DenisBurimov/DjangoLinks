from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('home', views.home, name='home'),
    path('add', views.add, name='add'),
    path('links', views.LinkView.as_view(), name='links'),
    path('about', views.about, name='about')
]