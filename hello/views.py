from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.gis.geoip2 import GeoIP2
import time
from .models import PageCounter

def index(request):
    counter, create = PageCounter.objects.get_or_create(page='index')
    counter.views += 1
    counter.save()
    client_address = request.META['HTTP_X_FORWARDED_FOR']
    g = GeoIP2()
    return HttpResponse("Hello, " + g.city(client_address)["city"] + "!  Server time is: " + time.strftime('%X') + " Page Views: " + str(counter.views))
