from django.conf.urls import url

from . import views

app_name = "teams"

urlpatterns = [
    url(r'^$', views.team_list, name='list'),
    url(r'^(?P<pk>\d+)/$', views.team_detail, name='detail'),
]
