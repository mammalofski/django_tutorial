from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView, ListView
from django.http import Http404, HttpResponseBadRequest
from django.db.models import Count, Sum, Avg, Prefetch
from rest_framework import generics

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from rest_framework import mixins
from rest_framework import permissions


# Create your views here.
from .models import *
from . import serializers


# class ModelViewSet(mixins.CreateModelMixin,
#                    mixins.RetrieveModelMixin,
#                    mixins.UpdateModelMixin,
#                    mixins.DestroyModelMixin,
#                    mixins.ListModelMixin,
#                    GenericViewSet):
#     """
#     A viewset that provides default `create()`, `retrieve()`, `update()`,
#     `partial_update()`, `destroy()` and `list()` actions.
#     """
#     pass
class IsOwner(permissions.BasePermission):
    def has_permission(self, request, view):
        if int(request.data['owner']) == request.user.id:
            return True
        return False
        # serializer = PostSerializer(data=request.data)
        # serializer.is_valid(raise_exception=True)
        # if serializer.data['owner'] == request.user:
        #     return True
        # return False


class PostViewSet(viewsets.ModelViewSet):
    permission_classes = (IsOwner, permissions.IsAdminUser)
    queryset = Post.objects.filter(deleted=False)
    serializer_class = serializers.PostSerializer

    def perform_destroy(self, instance):
        instance.deleted = True
        instance.save()




class ListCreatePost(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = serializers.PostSerializer

    def get_queryset(self):
        return self.queryset.filter(deleted=False)


class RetrieveUpdateDestroyPost(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = serializers.PostSerializer

    def get_queryset(self):
        return self.queryset.filter(deleted=False)


class ListCreateComment(generics.ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = serializers.CommentSerializer

    def get_queryset(self):
        return self.queryset.filter(deleted=False, post_id=self.kwargs.get('post_pk'))


class RetrieveUpdateDestroyComment(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = serializers.CommentSerializer

    def get_queryset(self):
        return self.queryset.filter(deleted=False)


class PostListCreate(APIView):
    def get(self, request):
        posts = Post.objects.filter(deleted=False)
        serializer = serializers.PostSerializer(posts, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = serializers.PostSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)







def user_posts(request, username):
    q = request.GET.get('qs')
    ex = request.GET.get('ex')
    # user = get_object_or_404(User, username=username)
    all_posts = Post.objects.filter(owner__username=username).prefetch_related(Prefetch('comments', queryset=Comment.objects.filter(deleted=False).annotate(no_of_likes=Count('likes')), to_attr='all_comments')).annotate(no_of_likes=Count('likes'))
    all_likes = all_posts.aggregate(all_likes=Sum('no_of_likes'))
    print(all_likes)
    # print(all_posts['all_likes'])

    if q:
        all_posts = all_posts.filter(content__icontains=q)
    if ex:
        all_posts = all_posts.exclude(content__icontains=ex)
    return render(request, 'faceapp/posts.html', {'posts': all_posts})


# def user_posts_search(request, username, query):
#     # user = get_object_or_404(User, username=username)
#     all_posts = Post.objects.filter(owner__username=username, content__icontains=query).prefetch_related('comments')
#     return render(request, 'faceapp/posts.html', {'posts': all_posts})


def user_home(request):
    p = request.GET.get('p')
    user = request.user
    relations = Relation.objects.filter(follower_id=user.id).values_list('followed_by_id', flat=True)
    posts = Post.objects.filter(owner_id__in=relations, deleted=False).values('id', 'content')
    if p:
        p = int(p)
        posts = posts[10 * (p - 1): 10 * p]
    return render(request, 'faceapp/user_home.html', {'posts': posts})


