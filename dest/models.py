from django.db import models
from django.utils import timezone
import datetime as dt


class Country(models.Model):
    name = models.CharField(max_length=120)
    image = models.ImageField(upload_to='media', null=True, blank=True)
    popular = models.BooleanField(default=False)

    class Meta:
        verbose_name_plural = 'Countries'

    @property
    def destination_count(self):
        return self.destination_set.count()

    def __str__(self):
        return self.name


class Destination(models.Model):
    name = models.CharField(max_length=120)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='media', blank=True, null=True)
    rating = models.IntegerField()
    price = models.IntegerField()
    description = models.TextField()
    popular = models.BooleanField(default=False)
    travel_date = models.DateField(default=(timezone.now() + dt.timedelta(days=7)))
    completed = models.BooleanField(default=False)
    date_completed = models.DateField(blank=True, null=True)

    class Meta:
        ordering = ['travel_date']

    def __str__(self):
        return f'{self.name} ({self.country})'


class Review(models.Model):
    destination = models.ForeignKey(Destination, on_delete=models.CASCADE)
    message = models.TextField()
