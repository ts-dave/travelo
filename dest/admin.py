from django.contrib import admin
from .models import *


class DestinatinationAdmin(admin.ModelAdmin):
    list_display = ('name', 'country', 'travel_date', 'price', 'completed')
    list_per_page = 40
    date_hierarchy = 'travel_date'
    search_fields = ('name',)
    list_filter = ('country',)


class CountryAdmin(admin.ModelAdmin):
    list_display = ('name', 'destination_count')


admin.site.register(Country, CountryAdmin)
admin.site.register(Destination, DestinatinationAdmin)
admin.site.register(Review)
admin.site.register(Day)
