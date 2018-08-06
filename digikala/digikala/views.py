from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, "index.html", {})

# def index(request):
#     return HttpResponse('my first django project')