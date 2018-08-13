from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


# Create your models here.


class Post(models.Model):
    content = models.CharField(max_length=240)
    owner = models.ForeignKey(User, related_name='posts', on_delete=models.CASCADE)
    created_date_time = models.DateTimeField(default=timezone.now)
    deleted = models.BooleanField(default=False)
    # image = models.ImageField(blank=True, null=True)


class Group(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=255, blank=True, null=True)
    users = models.ManyToManyField(User)


class Comment(models.Model):
    user = models.ForeignKey(User, related_name='comments', on_delete=models.CASCADE)
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    content = models.CharField(max_length=127)
    deleted = models.BooleanField(default=False)
    created_date_time = models.DateTimeField(default=timezone.now)


class Like(models.Model):
    user = models.ForeignKey(User, related_name='likes', on_delete=models.CASCADE)
    post = models.ForeignKey(Post, related_name='likes', on_delete=models.CASCADE, blank=True, null=True)
    comment = models.ForeignKey(Comment, related_name='likes', on_delete=models.CASCADE, blank=True, null=True)


class Relation(models.Model):
    follower = models.ForeignKey(User, related_name='followers', on_delete=models.CASCADE)
    followed_by = models.ForeignKey(User, related_name='followings', on_delete=models.CASCADE)


class DirectMessage(models.Model):
    sender = models.ForeignKey(User, related_name='senders', on_delete=models.CASCADE)
    receiver = models.ForeignKey(User, related_name='receivers', on_delete=models.CASCADE)
    message = models.CharField(max_length=127)
    created_date_time = models.DateTimeField(default=timezone.now)

















