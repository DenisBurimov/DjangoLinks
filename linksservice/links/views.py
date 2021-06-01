from django.shortcuts import render, redirect
import pyshorteners
from .models import Link
from .forms import CreateLink

def home(request):
    data = {
        'page_title' : 'Home Page',
        'articles' : 'Articles.objects.all()',
    }

    return render(request, 'links/home.html', data)

def links(request):
    if request.method == "POST":
        form = CreateLink(request.POST)
        if form.is_valid():

            form.save()
            obj = Link()
            obj.full_link = form.cleaned_data.get('full_link')
            obj.author = request.user
            obj.save()
            return redirect('links')
    else:
        form = CreateLink()

    if request.user.is_authenticated:
        available_links = Link.objects.filter(author=request.user)
    else:
        available_links = Link.objects.all()

    data = {
        'page_title' : 'Links',
        'form': form,
        'available_links': available_links,
    }

    return render(request, 'links/links.html', data)

def about(request):
    data = {
        'page_title' : 'About',
    }

    return render(request, 'links/about.html', data)
