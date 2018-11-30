from django.shortcuts import render
from django.views.generic import View, ListView
from . import models


def music_list(request):
    # musics = models.Song.objects.all()
    albums = models.Album.objects.all().prefetch_related('songs')
    print(albums)
    return render(request, 'music/music-list.html', {'albums': albums})


def album_detail(request, id):
    album = models.Album.objects.filter(id=id).prefetch_related('songs')
    print(id)
    print(album)
    album = album[0]
    return render(request, 'music/album_detail.html', {'album': album})

