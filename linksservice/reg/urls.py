from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('registration', views.registration, name='registration'),
    path('profile', views.profile, name='profile'),
    path('login', auth_views.LoginView.as_view(template_name='reg/login.html'), name='login'),
    path('logout', auth_views.LogoutView.as_view(template_name='reg/logout.html'), name='logout')
]