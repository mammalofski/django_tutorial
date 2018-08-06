from django.shortcuts import render
from django.http import HttpResponse
from .models import *

# Create your views here.

def laptops(request):
    laptops = Laptop.objects.all()
    return HttpResponse('my first laptop is : %d %f' % (laptops[0].brand, laptops[0].weight))
