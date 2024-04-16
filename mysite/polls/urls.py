from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('some_url', views.some_url, name='index'),
    path('weather', views.VilageFcstInfoService, name='weather')
]
