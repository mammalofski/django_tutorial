from django.shortcuts import render
from . import models


def music_list(request):
    musics = models.Song.objects.all()
    return render(request, 'music/music-list.html', {'musics': musics})

