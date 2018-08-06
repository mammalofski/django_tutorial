from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import *

# Create your views here.


def laptops(request):
    laptops = Laptop.objects.all()

    return render(request, "inventory/laptops.html", {
        "laptops": laptops
    })


def laptop(request, id):
    # laptop = Laptop.objects.get(id=id)
    laptop = get_object_or_404(Laptop, id=id)
    return HttpResponse(str(laptop))

