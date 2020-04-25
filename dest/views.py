from django.shortcuts import render, HttpResponse
from django.shortcuts import get_object_or_404
from .models import *
import random


def homepage(request):
    popular_countries = Country.objects.filter(popular=True)
    popular_countries = random.choices(popular_countries, k=6)
    
    popular_places = Destination.objects.filter(popular=True)
    popular_places = random.choices(popular_places, k=6)
    
    context = {
        'popular_countries': popular_countries,
        'popular_places': popular_places,
   }
    return render(request, 'dest/index.html', context)


def country_destinations(request, pk):
    country = get_object_or_404(Country, pk=pk)
    context = {
        'country': country,
    }
    return render(request, 'dest/country_destination.html', context)


def about(request):
    return render(request, 'dest/about.html')


def destination(request):
    destinations = list(Destination.objects.all())
    dests = random.choices(destinations, k=6)
    context = {
        'dests': dests,
    }
    return render(request, 'dest/travel_destination.html', context)


def destination_detail(request, pk):
    destination = get_object_or_404(Destination, pk=pk)
    context = {
        'destination': destination,
    }
    return render(request, 'dest/destination_details.html', context)


def register(request):
    return HttpResponse('Registration Page')


def login(request):
    return HttpResponse('login page')


def logout(request):
    return HttpResponse('logout page')


def contact(request):
    return render(request, 'dest/contact.html')
