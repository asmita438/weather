import requests
from django.shortcuts import render

# Create your views here.
def index(request):
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid='6e86ee02f0d6728b3bc4a28eee4676d1'
    city = 'Kathmandu'