from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm
from django.contrib.auth.decorators import login_required


def registration(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Аккаунт для {username} создан')
            return redirect('login')
    else:
        form = UserRegisterForm()

    data = {
        'page_title' : 'Registration',
        'form' : form
    }

    return render(request, 'reg/registration.html', data)

@login_required
def profile(request):
    data = {
        'page_title' : 'Profile',
    }

    return render(request, 'reg/profile.html', data)
