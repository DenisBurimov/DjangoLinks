from django.shortcuts import render
import pyshorteners
from .models import Link

def home(request):
    data = {
        'page_title' : 'Home Page',
        'articles' : 'Articles.objects.all()',
    }

    return render(request, 'links/home.html', data)

def links(request):
    if request.user.is_authenticated:
        available_links = Link.objects.filter(author=request.user)
    else:
        available_links = Link.objects.all()

    data = {
        'page_title' : 'Links',
        'available_links': available_links,
    }

    return render(request, 'links/links.html', data)

def add(request):
    full_link = request.POST["full_link"]
    cut = pyshorteners.Shortener()
    cutted_link = cut.tinyurl.short(full_link)

    data = {
        'page_title': 'One',
        'cutted_link': cutted_link
    }

    return render(request, 'links/add.html', data)

def about(request):
    data = {
        'page_title' : 'About',
    }

    return render(request, 'links/about.html', data)