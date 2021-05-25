from django.shortcuts import render

def home(request):
    data = {
        'page_title' : 'Home Page',
        'articles' : 'Articles.objects.all()',
    }

    return render(request, 'links/home.html', data)

def links(request):
    data = {
        'page_title' : 'Links',
    }

    return render(request, 'links/links.html', data)

def about(request):
    data = {
        'page_title' : 'About',
    }

    return render(request, 'links/about.html', data)