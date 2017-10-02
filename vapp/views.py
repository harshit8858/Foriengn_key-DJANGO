from django.shortcuts import render
from datetime import *
from .models import *
from .forms import *
from django.http import *


def index(request):
    pub = Publisher.objects.all()

    return render(request, 'home.html', {'pub': pub})

def pub_form(request):
    if request.method == 'POST':
        form = Publisherform(request.POST)

        if form.is_valid():
            form.save()

            return HttpResponseRedirect('/')

    else:
        form = Publisherform()

    return render(request, 'pub_form.html', {'form':form})

def book_form(request):
    if request.method == 'POST':
        form = Bookform(request.POST)

        if form.is_valid():
            form.save()

            return HttpResponseRedirect('/')

    else:
        form = Bookform()

    return render(request, 'book_form.html', {'form': form})
