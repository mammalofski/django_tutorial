from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView, ListView
from django.http import Http404

# Create your views here.
from .models import *


# class UserHomeView(DetailView)


def user_posts(request, username):
    user = get_object_or_404(User, username=username)
    all_posts = Post.objects.filter(owner=user).prefetch_related('comments')
    return render(request, 'faceapp/posts.html', {'posts': all_posts})


def user_home(request):
    relations = Relation.objects.filter(follower=request.user).values_list('followed_by', flat=True)
    all_posts = Post.objects.filter(owner__in=relations)
    return render(request, 'faceapp/user_home.html', {'posts': all_posts})



