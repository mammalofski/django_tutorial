from django.urls import path, include
from . import views

urlpatterns = [
    path('post/', views.ListCreatePost.as_view(), name='post_list'),
    path('post/<int:pk>', views.RetrieveUpdateDestroyPost.as_view(), name='post_detail'),
    path('post/<int:post_pk>/comment/', views.ListCreateComment.as_view(), name='comment_list'),
    # path('home/', views.user_home),
    # path('user/<str:username>', views.user_posts),
]
