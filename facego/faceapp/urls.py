from django.urls import path, include
from . import views

urlpatterns = [
    path('home/', views.user_home),
    path('user/<str:username>', views.user_posts),
]
