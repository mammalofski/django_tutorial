from django.http import HttpResponse

def index(request):
    return HttpResponse('my first django project')