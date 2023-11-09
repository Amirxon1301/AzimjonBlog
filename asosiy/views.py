from django.shortcuts import render
from .models import *


def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def blog(request):
    data = {
        "maqolalar" : Maqola.objects.all()
    }
    return render(request, 'blog.html', data)

def maqola(request, link):
    data = {
        "maqola" : Maqola.objects.filter(slug=link)
    }
    return render(request, 'maqola.html')


