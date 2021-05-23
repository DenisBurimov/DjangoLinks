from django.shortcuts import render

def home(request):
    data = {
        'page_title' : 'Home Page',
        'articles' : 'Articles.objects.all()',
    }

    return render(request, 'links/home.html', data)

def contacts(request):
    data = {
        'page_title' : 'Contact Us',
        'contacts' : 'denysburimov@gmail.com'
    }

    return render(request, 'links/contacts.html', data)