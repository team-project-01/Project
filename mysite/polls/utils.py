import urllib.request
import xml.dom.minidom
from datetime import datetime, timedelta
from .models import forecastData , Rainpercent , Wind

index_number = {
    90: (87, 140),
    95: (75, 143),
    98: (61, 134),
    99: (55, 130),
    100: (89, 130),
    101: (73, 134),
    105: (92, 132),
    106: (96, 126),
    108: (63, 126),
    112: (38, 129),
    114: (77, 122),
    119: (62, 121),
    121: (82, 121),
    127: (76, 115),
    129: (51, 109),
    130: (102, 114),
    131: (69, 108),
    133: (59, 77),
    135: (78, 98),
    136: (95, 77),
    137: (79, 65),
    138: (103, 95),
    140: (55, 92),
    143: (57, 60),
    146: (62, 89),
    152: (99, 83),
    155: (93, 74),
    156: (63, 122),
    159: (59, 65),
    162: (87, 68),
    165: (51, 67),
    168: (74, 68),
    170: (61, 56),
    172: (55, 82),
    174: (70, 70),
    177: (54, 105),
    184: (50, 32),
    185: (64, 92),
    188: (92, 131),
    189: (50, 32),
    192: (81, 75),
    201: (47, 128),
    202: (70, 124),
    203: (68, 121),
    211: (82, 134),
    212: (84, 132),
    216: (96, 118),
    217: (90, 125),
    221: (81, 118),
    226: (73, 105),
    232: (63, 111),
    235: (52, 99),
    236: (61, 98),
    238: (81, 76),
    239: (70, 121),
    243: (48, 84),
    244: (67, 83),
    245: (48, 32),
    247: (56, 33),
    248: (88, 110),
    251: (55, 82),
    252: (45, 75),
    253: (93, 76),
    254: (63, 81),
    257: (99, 80),
    258: (61, 65),
    259: (58, 59),
    260: (60, 59),
    261: (49, 64),
    262: (69, 60),
    263: (84, 81),
    264: (73, 83),
    266: (74, 70),
    268: (44, 55),
    271: (96, 116),
    272: (88, 111),
    273: (81, 106),
    276: (96, 105),
    277: (102, 106),
    278: (86, 103),
    279: (85, 95),
    281: (54, 33),
    283: (101, 90),
    284: (78, 88),
    285: (81, 83),
    288: (92, 83),
    289: (79, 80),
    294: (91, 69),
    295: (79, 68)
}

def today_weather_data(index):
    nx, ny = index_number[index]
    encodingKey = 'QkWF79xLl9MK1KDi2VAOG%2Fq8vEgL%2BCMNmgYBxF23Hei%2FIfa4VMfNNOs8TFUlS2PcgDVg2AOwexAou5Ffl5C43w%3D%3D'

    now = datetime.now() + timedelta(hours=9)
    base_date = datetime.today().strftime("%Y%m%d")
    update_time = [2,5,8,11,14,17,20,23]
    #단기예보
    #Base_time : 0200, 0500, 0800, 1100, 1400, 1700, 2000, 2300 (1일 8회)
    #API 제공 시간(~이후) : 02:10, 05:10, 08:10, 11:10, 14:10, 17:10, 20:10, 23:10
    if now.hour in update_time and now.minute > 11:
        #10분에 바로 업데이트가 안될 수도 있으므로 12분으로 잡아둠
        if now.hour < 10:
            base_time = f'0{now.hour}00'
        else :
            base_time = f'{now.hour}00'
    else :
        if 2 < now.hour < 5 : base_time = '0200'
        elif 5 < now.hour < 8 : base_time = '0500'
        elif 8 < now.hour < 11 : base_time = '0800'
        elif 11 < now.hour < 14 : base_time = '1100'
        elif 14 < now.hour < 17 : base_time = '1400'
        elif 17 < now.hour < 20 : base_time = '1700'
        elif 20 < now.hour < 23 : base_time = '2000'
        elif 23 < now.hour : base_time = '2300'
        else : 
            base_time = '2300'
            base_date = (datetime.today() - timedelta(days=1)).strftime("%Y%m%d")
    

        
    url = "http://apis.data.go.kr/1360000/VilageFcstInfoService_2.0/getVilageFcst?ServiceKey=" + \
    encodingKey + \
    '&pageNo=1&numOfRows=100&dataType=XML' + \
    f'&base_date={base_date}' + \
    f'&base_time={base_time}' + \
    f'&nx={nx}&ny={ny}'
        
        #할일 1. url 두개에서 크롤해온 데이터를 데이터필드에 넣어주기 , 같은 정보 저장 안되게 하기 :done
        #할일 0. weather 들어가면 데이터 바로 불러와지도록. :done
        #할일 2. 날짜별, 시간별로 구분한 데이터를 지역별로 구분해주기 
        #할일 3. 다대 다 필드 구성 :done
        #할일 4. 인코딩 키 숨기기
        
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
            result += f'{fcstDate} {fcstTime}시 {category} : {fcstValue}\n'
            if category == 'TMP':
                result += f"{fcstDate[:4]}년 {fcstDate[4:6]}월 {fcstDate[6:]}일 {fcstTime} 시의 온도는 {fcstValue}도 이다. <br>"  # 예보 날짜, 시간, 값, 카테고리를 문자열에 추가하고 각 값 뒤에 줄바꿈 추가
                # 데이터베이스에 저장
                if forecastData.objects.filter(fcstDate=fcstDate, fcstTime=fcstTime, fnx=nx, fny=ny).exists():  # 이미 해당 날짜, 시간, nx, ny의 데이터가 존재하면
                    forecastData.objects.filter(fcstDate=fcstDate, fcstTime=fcstTime, fnx=nx, fny=ny).delete()  # 해당 데이터 삭제
                forecast = forecastData()  # 새 객체 생성
                forecast.fcstDate = fcstDate
                forecast.fcstTime = fcstTime
                forecast.fcstValue = fcstValue
                forecast.fnx = nx
                forecast.fny = ny
                forecast.save()  # 객체 저장
            if category == 'POP': 
                gangsu = Rainpercent()
                gangsu.fcstDate = fcstDate
                gangsu.fcstTime = fcstTime
                gangsu.fcstValue = fcstValue
                gangsu.fnx = nx
                gangsu.fny = ny
                gangsu.save()
            if category == 'WSD':
                wwind = Wind()
                wwind.fcstDate = fcstDate
                wwind.fcstTime = fcstTime
                wwind.fcstValue = fcstValue
                wwind.fnx = nx
                wwind.fny = ny
                wwind.save()
            
        return url
    else: # 실패시 -> 에러코드 출력
        res = dom.getElementsByTagName('resultMsg')
        return f"Error Code: {res}"
    

def yesterday_weather_data(index):
    nx, ny = index_number[index]
    yesterday = (datetime.today() - timedelta(days=1)).strftime("%Y%m%d")
    start = (datetime.today() - timedelta(days=8)).strftime("%Y%m%d")
    
    encodingKey = 'QkWF79xLl9MK1KDi2VAOG%2Fq8vEgL%2BCMNmgYBxF23Hei%2FIfa4VMfNNOs8TFUlS2PcgDVg2AOwexAou5Ffl5C43w%3D%3D'
    
    url = "http://apis.data.go.kr/1360000/AsosHourlyInfoService/getWthrDataList?serviceKey=" + \
    encodingKey + \
    '&numOfRows=999&pageNo=1&dataCd=ASOS&dateCd=HR' + \
    f'&stnIds={index}&endDt={yesterday}&endHh=23' + \
    f'&startHh=01&startDt={start}'

    
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
                if forecastData.objects.filter(fcstDate=fcstDate, fcstTime=fcstTime, fnx=nx, fny=ny).exists():  # 이미 해당 날짜, 시간, nx, ny의 데이터가 존재하면
                    forecastData.objects.filter(fcstDate=fcstDate, fcstTime=fcstTime, fnx=nx, fny=ny).delete()  # 해당 데이터 삭제
                forecast = forecastData()  # 새 객체 생성
                forecast.fcstDate = fcstDate
                forecast.fcstTime = fcstTime
                forecast.fcstValue = fcstValue
                forecast.fnx = nx
                forecast.fny = ny
                forecast.save()  # 객체 저장
            if category == 'POP':
                if forecastData.objects.filter(fcstDate=fcstDate, fcstTime=fcstTime, fnx=nx, fny=ny).exists():  # 이미 해당 날짜, 시간, nx, ny의 데이터가 존재하면
                    forecastData.objects.filter(fcstDate=fcstDate, fcstTime=fcstTime, fnx=nx, fny=ny).delete()
                gangsu = Rainpercent()
                gangsu.fcstDate = fcstDate
                gangsu.fcstTime = fcstTime
                gangsu.fcstValue = fcstValue
                gangsu.fnx = nx
                gangsu.fny = ny
                gangsu.save()
            if category == 'WSD':
                if forecastData.objects.filter(fcstDate=fcstDate, fcstTime=fcstTime, fnx=nx, fny=ny).exists():  # 이미 해당 날짜, 시간, nx, ny의 데이터가 존재하면
                    forecastData.objects.filter(fcstDate=fcstDate, fcstTime=fcstTime, fnx=nx, fny=ny).delete()
                wwind = Wind()
                wwind.fcstDate = fcstDate
                wwind.fcstTime = fcstTime
                wwind.fcstValue = fcstValue
                wwind.fnx = nx
                wwind.fny = ny
                wwind.save()
            
        return rescode
    else: # 실패시 -> 에러코드 출력
        res = dom.getElementsByTagName('resultMsg')
        return f"Error Code: {res}"