from django.urls import path
from . import views


app_name = 'dest'

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('about/', views.about, name='aboutpage'),
    path('country/<int:pk>/', views.country_destinations, name='country_destinations'),
    path('destination/', views.destination, name='destination'),
    path('destination/<int:pk>/', views.destination_detail, name='destination_detail'),
    path('contact/', views.contact, name='contactpage'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('register', views.register, name='register'),
    path('search/', views.search, name='search'),
]