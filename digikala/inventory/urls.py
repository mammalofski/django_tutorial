
from django.urls import path
# from .views import laptops
from . import views

urlpatterns = [
    path('laptop/', views.laptops,name='laptops'),
    path('laptop/<int:id>/', views.laptop)
]
