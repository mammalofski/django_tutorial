from django.urls import path
from . import views

urlpatterns = [
    path('', views.music_list),
    path('<int:id>', views.album_detail)
]
