from django.shortcuts import render

def registration(request):
    data = {
        'page_title' : 'Registration',
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