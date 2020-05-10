from django.shortcuts import render, HttpResponse
from django.shortcuts import get_object_or_404
from .forms import SubscriberForm
from .models import Country, Destination, Day, Subscriber
import random


def homepage(request):
    form = SubscriberForm()
    
    if request.method == 'POST':
        form = SubscriberForm(request.POST)
        print(form)
        if form.is_valid():
            form.save()
    
    popular_countries = Country.objects.filter(popular=True)
    popular_countries = random.sample(list(popular_countries), k=6)
    
    popular_places = Destination.objects.filter(popular=True)
    popular_places = random.sample(list(popular_places), k=6)
    
    context = {
        'form': form,
        'popular_countries': popular_countries,
        'popular_places': popular_places,
   }
    return render(request, 'dest/index.html', context)


def search(request):
    place = request.GET['place']
    #date = request.GET['date']
    travel_type = request.GET.get('travel_type')
    
    dests = Destination.objects.filter(name__contains=place)
    context = {
        'dests': dests,
        'travel_type': travel_type,
    }
    return render(request, 'dest/travel_destination.html', context)


def country_destinations(request, pk):
    country = get_object_or_404(Country, pk=pk)
    context = {
        'country': country,
    }
    return render(request, 'dest/country_destination.html', context)


def about(request):
    return render(request, 'dest/about.html')


def destination(request):
    destinations = Destination.objects.all()
    dests = random.sample(list(destinations), k=6)
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
