from django.http import HttpResponse
import urllib.request
from xml.dom.minidom import parseString
import xml.dom.minidom
from .models import forecastData , Rainpercent , Wind
from django.shortcuts import render
# Create your views here.

def index(request) :
    month_text = request.GET.get('sido')
    #board_list = Board.objects.filter(month=month_text)
    return render(request, 'index.html')



def some_url(request) :
    return HttpResponse('some url구현')


def VilageFcstInfoService(a):
    encodingKey = 'QkWF79xLl9MK1KDi2VAOG%2Fq8vEgL%2BCMNmgYBxF23Hei%2FIfa4VMfNNOs8TFUlS2PcgDVg2AOwexAou5Ffl5C43w%3D%3D'
    # request url 정의

    url = "http://apis.data.go.kr/1360000/VilageFcstInfoService_2.0/getVilageFcst?ServiceKey=" + \
    encodingKey + \
    '&pageNo=1&numOfRows=1000&dataType=XML' + \
    '&base_date=20240415' + \
    '&base_time=0200' + \
    '&nx=60&ny=127'
    
    request = urllib.request.Request(url)
    response = urllib.request.urlopen(request)

    rescode = response.getcode()
    
    if (rescode == 200): # 요청 결과 성공시에만
        response_body = response.read()
        res = xml.dom.minidom.parseString(response_body.decode('utf-8'))
        pretty_res = res.toprettyxml()
        dom = xml.dom.minidom.parseString(pretty_res)
        tag_name = 'item'  
        elements = dom.getElementsByTagName(tag_name)
        result = ""
        for elem in elements:  # 각 'item' 요소에 대해
            fcstDate = elem.getElementsByTagName('fcstDate')[0].firstChild.data
            fcstTime = elem.getElementsByTagName('fcstTime')[0].firstChild.data[:2]
            fcstValue = elem.getElementsByTagName('fcstValue')[0].firstChild.data
            category = elem.getElementsByTagName('category')[0].firstChild.data
            if category == 'TMP':
                result += f"{fcstDate[:4]}년 {fcstDate[4:6]}월 {fcstDate[6:]}일 {fcstTime} 시의 온도는 {fcstValue}도 이다. <br>"  # 예보 날짜, 시간, 값, 카테고리를 문자열에 추가하고 각 값 뒤에 줄바꿈 추가
                # 데이터베이스에 저장
                forecast = forecastData()  # 새 객체 생성
                forecast.fcstDate = fcstDate
                forecast.fcstTime = fcstTime
                forecast.fcstValue = fcstValue
                forecast.save()  # 객체 저장
            if category == 'POP': 
                gangsu = Rainpercent()
                gangsu.fcstDate = fcstDate
                gangsu.fcstTime = fcstTime
                gangsu.fcstValue = fcstValue
                gangsu.save()
            if category == 'WSD':
                wwind = Wind()
                wwind.fcstDate = fcstDate
                wwind.fcstTime = fcstTime
                wwind.fcstValue = fcstValue
                wwind.save()
            
        return HttpResponse(result)  # 문자열을 HttpResponse에 전달
    else: # 실패시 -> 에러코드 출력
        return HttpResponse("Error Code:" + str(rescode))