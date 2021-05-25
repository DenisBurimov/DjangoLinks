from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm

def registration(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Аккаунт для {username} создан')
            return redirect('home')
    else:
        form = UserRegisterForm()

    data = {
        'page_title' : 'Registration',
        'form' : form
    }

    return render(request, 'reg/registration.html', data)

def profile(request):
    data = {
        'page_title' : 'Profile',
    }

    return render(request, 'reg/profile.html', data)

def login(request):
    data = {
        'page_title' : 'Login',
    }

    return render(request, 'reg/login.html', data)

def logout(request):
    data = {
        'page_title' : 'Logout',
    }

    return render(request, 'reg/logout.html', data)