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

#결과 페이지 연결
@csrf_exempt
def result(request):
    area2 = int(request.POST['area2'])
    a = yesterday_weather_data(area2)
    b = today_weather_data(area2)
    # 모든 컨텍스트 변수를 하나의 딕셔너리로 합침
    context = {
        'area2': area2,
        'a': a,
        'b': b
    }
    return render(request, 'result.html', context)

@csrf_exempt
def fetch_weather(request): #어제꺼부터 받아와야 데이터가 꼬이지 않고 정렬됨
    area2 = int(request.POST['area2'])
    a = yesterday_weather_data(area2)
    b = today_weather_data(area2)

    answer = a + '<br><br><br>' + b
    return HttpResponse(answer)


def graph(request):
    context = {'place': '서울'}
    # 템플릿에 context를 전달
    return render(request, 'polls/graph.html', context)
