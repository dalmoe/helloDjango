from django.shortcuts import render
from django.http import HttpResponse
import time
from .models import PageCounter

def index(request):
    counter, create = PageCounter.objects.get_or_create(page='index')
    counter.views += 1
    counter.save()
    return HttpResponse("Hello, world! " + time.strftime('%X') + " " + str(counter.views) + "views")
