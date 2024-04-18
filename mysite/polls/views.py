from django.http import HttpResponse
from django.shortcuts import render
from .utils import today_weather_data, yesterday_weather_data
# Create your views here.

def index(request) :
    return HttpResponse('Hello')



def some_url(request) :
    return HttpResponse('some url구현')


def fetch_weather(request): #어제꺼부터 받아와야 데이터가 꼬이지 않고 정렬됨
    
    a = yesterday_weather_data(108)
    b = today_weather_data(108)

    answer = a + '<br><br><br>' + b
    return HttpResponse(answer)