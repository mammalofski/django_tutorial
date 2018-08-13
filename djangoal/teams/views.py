from django.shortcuts import render, get_object_or_404
from django.views.generic import (
    ListView, DetailView, CreateView
)

from django.contrib.auth.mixins import LoginRequiredMixin

from . import models


# def team_list(request):
#    teams = models.Team.objects.all()
#    return render(request, 'teams/team_list.html', {'teams': teams})



class TeamListView(LoginRequiredMixin, ListView):
    template_name = "teams/team_list.html"
    model = models.Team
    context_object_name = "teams"

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.all()[:5]
        return queryset


# def team_detail(request, pk):
#    team = get_object_or_404(models.Team, pk=pk)
#    return render(request, 'teams/team_detail.html', {'team': team})


class TeamDetailView(DetailView):
    model = models.Team


class TeamCreateView(CreateView):
    model = models.Team
    fields = ('name', 'coach', 'practice_location')
