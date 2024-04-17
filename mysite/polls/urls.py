from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('weather/', views.VilageFcstInfoService, name='weather'),
    path('test/', views.graph, name='graph'),
    path('result', views.result, name='result'),
]
