from __future__ import unicode_literals

from django.db import models

# Create your models here.
class searchData(models.Model):
    name = models.CharField(max_length=128)
    address = models.CharField(max_length=256)
    terms = models.CharField(max_length=1024)
    
