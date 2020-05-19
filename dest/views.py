from django.shortcuts import render, HttpResponse, redirect
from django.shortcuts import get_object_or_404
from django.utils import timezone
from .forms import SubscriberForm
from .models import Country, Destination, Day, Subscriber
import random


def homepage(request):
    form = SubscriberForm()
    
    if request.method == 'POST':
        form = SubscriberForm(request.POST)

        if form.is_valid():
            form.save()
        return redirect('/')
    
    popular_countries = Country.objects.filter(popular=True).prefetch_related('destination_set')
    popular_countries = random.sample(list(popular_countries), k=6)
    
    popular_places = Destination.objects.filter(popular=True).prefetch_related('day_set','review_set')
    popular_places = random.sample(list(popular_places), k=6)
    
    recents = Destination.objects.filter(completed=True)
    # recent = random.sample(list(recent), k=3)ls
    
    context = {
        'form': form,
        'recents': recents,
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


def contact(request):
    return render(request, 'dest/contact.html')
