from __future__ import unicode_literals

from django.db import models

# Create your models here.
class PageCounter(models.Model):
    page = models.CharField(max_length=32, default='default')
    
    views = models.IntegerField(default=0)
    
    