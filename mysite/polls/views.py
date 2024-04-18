from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .utils import today_weather_data, yesterday_weather_data,get_weather_image, index_num_dic
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

# 기본 페이지 연결
def index(request) :
    area = request.GET.get('area')
    c,d = get_weather_image('강수량')
    e,f = get_weather_image('기온')
    g,h = get_weather_image('바람')
    context = {'area': area, 'im' : c, 'im2' : d, 'im3' : e, 'im4' : f, 'im5' : g, 'im6' : h}
    return render(request, 'index.html', context)

#결과 페이지 연결
@csrf_exempt
def result(request):
    area2 = int(request.POST['area2'])
    a = yesterday_weather_data(area2)
    b = today_weather_data(area2)
    # 모든 컨텍스트 변수를 하나의 딕셔너리로 합침
    
    if area2 in index_num_dic:
        context = {'place': index_num_dic[area2],'today' : b, 'yesterday' : a ,}
    return render(request, 'result.html', context)

#그냥 잘 돌아가는지 확인하는 용 http~~~8000/weather 치면 나오는 것
def fetch_weather(request): #어제꺼부터 받아와야 데이터가 꼬이지 않고 정렬됨
    random = 108 #임의의 지역번호
    a = yesterday_weather_data(random)
    b = today_weather_data(random)

    answer = a + '<br><br><br>' + b
    return HttpResponse(answer)


def graph(request):
    context = {'place': "서울" }
    # 템플릿에 context를 전달
    return render(request, 'polls/graph.html', context)
