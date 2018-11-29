from django.db import models

# Create your models here.


class Artist(models.Model):
    name = models.CharField(max_length=100)
    birth = models.DateField()


class Album(models.Model):
    name = models.CharField(max_length=100)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE, related_name='albums')


class Song(models.Model):
    name = models.CharField(max_length=100)
    album = models.ForeignKey(Album, on_delete=models.CASCADE, related_name='songs', null=True, blank=True)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE, related_name='songs', null=True, blank=True)
