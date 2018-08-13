from django.conf.urls import url
from django.urls import path

from . import views

app_name = "teams"

urlpatterns = [
    path('', views.TeamListView.as_view(), name='list'),
    path('create/', views.TeamCreateView.as_view(), name='create'),
    path('<int:pk>/', views.TeamDetailView.as_view(), name='detail'),
]
