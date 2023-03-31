from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
]

from django.shortcuts import render

def home(request):
    return render(request, 'core/home.html')
