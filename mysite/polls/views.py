from django.http import HttpResponse
from django.shortcuts import render
from .utils import today_weather_data, yesterday_weather_data
# Create your views here.

def index(request) :
    return HttpResponse('Hello')



def some_url(request) :
    return HttpResponse('some url구현')


def fetch_weather(request):
    a = today_weather_data(108)
    return HttpResponse(a)