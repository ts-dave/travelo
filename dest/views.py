from django.shortcuts import render, HttpResponse
from django.shortcuts import get_object_or_404
from .models import *


def homepage(request):
    popular_countries = Country.objects.filter(popular=True)[:6]
    popular_places = Destination.objects.filter(popular=True)[:6]
    context = {
        'popular_countries': popular_countries,
        'popular_places': popular_places,
    }
    return render(request, 'dest/index.html', context)


def about(request):
    return render(request, 'dest/about.html')


def destination(request):
    return render(request, 'dest/travel_destination.html')


def destination_detail(request, pk):
    destination = get_object_or_404(Destination, pk=pk)
    context = {
        'destination': destination,
    }
    return HttpResponse('destination detail page', context)


def login(request):
    return HttpResponse('login page')


def logout(request):
    return HttpResponse('logout page')


def contact(request):
    return render(request, 'dest/contact.html')
