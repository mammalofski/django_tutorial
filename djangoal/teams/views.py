from django.shortcuts import render, get_object_or_404

from . import models


def team_list(request):
   teams = models.Team.objects.all()
   return render(request, 'teams/team_list.html', {'teams': teams})


def team_detail(request, pk):
   team = get_object_or_404(models.Team, pk=pk)
   return render(request, 'teams/team_detail.html', {'team': team})
