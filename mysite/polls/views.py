from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .utils import today_weather_data, yesterday_weather_data
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
# Create your views here.

# 기본 페이지 연결
def index(request) :
    area = request.GET.get('area')
    context = {'area': area,}
    print("HTML에서 넘어온 area: ", area)
    return render(request, 'index.html', area)

def some_url(request) :
    return HttpResponse('some url구현')

#결과 페이지 연결
@csrf_exempt
def result(request):
    area2 = request.POST['area2']
    return render(request, 'result.html', {'area2': area2})



def fetch_weather(request): #어제꺼부터 받아와야 데이터가 꼬이지 않고 정렬됨
    
    a = yesterday_weather_data(108)
    b = today_weather_data(108)

    answer = a + '<br><br><br>' + b
    return HttpResponse(answer)
    
def graph(request):
    context = {'place': '서울'}
    # 템플릿에 context를 전달
    return render(request, 'polls/graph.html', context)
