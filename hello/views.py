from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.gis.geoip2 import GeoIP2
from django.conf import settings
import json
import time
import urllib2
from .models import PageCounter



def index(request):
    counter, create = PageCounter.objects.get_or_create(page='index')
    counter.views += 1
    counter.save()
    client_address = request.META['HTTP_X_FORWARDED_FOR']
    g = GeoIP2()
    weather = getWeather(g.city(client_address))
    temp = (weather["temp"] - 273.15) * 1.8000 + 32.0
    return HttpResponse("Hello, " + g.city(client_address)["city"] + "!  Server time is: " + time.strftime('%X') + " Page Views: " + str(counter.views) + " Temperature is " + str(temp) + u'\N{DEGREE SIGN}' + "F")
    
    
def getWeather(city):
    url = "http://api.openweathermap.org/data/2.5/weather?zip="
    url += city["postal_code"]
    url += ","
    url += city["country_code"]
    url += "&APPID=2e02476a080baa6b5c05c96868900cca"
    response = urllib2.urlopen(url)
    weather = json.loads(response.read())
    return weather["main"]
