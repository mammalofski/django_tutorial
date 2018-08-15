from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView
from django.http import Http404

# Create your views here.
from .models import *


# class UserHomeView(DetailView)


def user_home(request, username):
    user = get_object_or_404(User, username=username)
    all_posts = Post.objects.filter(owner=user)
    return render(request, 'faceapp/posts.html', {'posts': all_posts})



