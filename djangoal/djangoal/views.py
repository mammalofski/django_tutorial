from django.shortcuts import render
from django.views.generic import View, TemplateView
from django.http import HttpResponse


# def home(request):
#    return render(request, 'home.html')


class HomeView(TemplateView):
   template_name = 'home.html'

   def get_context_data(self, **kwargs):
      context = super().get_context_data(**kwargs)
      context["no_of_games_today"] = 5
      return context


class HelloWorldView(View):
   def get(self, request):
      return HttpResponse("Helo world!")


