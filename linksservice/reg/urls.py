from django.urls import path
from . import views

urlpatterns = [
    path('registration', views.registration, name='registration'),
    path('profile', views.profile, name='profile'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout')
]