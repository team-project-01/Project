#%%
import matplotlib.pyplot as plt
import numpy as np
#from django.utils import timezone
import time
import datetime
from dateutil.relativedelta import relativedelta
from .models import *
import os
from datetime import timedelta

############## 
### 날씨 데이터를 그래프화하고 이를 png로 저장합니다.
#
### random data => 크롤한 데이터로 바꿔야합니다.
### 비교 데이터를 yesterday라고만 표시해뒀습니다.
#
### 수하님 저 둘다 그래프 만들어보고 나은걸로 선택하기로 했습니다.
### 1일전, 2일전, 7일전을 선택해서 비교가능하게 구현한다고 생각하고 만들어봤습니다.
### (의도와 맞지 않을 시 수정하거나 수하님 그래프 사용)
##############

#### 데이터필드에 맞춰 함수명 변경했습니다.


#temps=[float(i[3]) for i in forecastData.objects.filter(fcstDate='20240417').values_list()]
#                    단위값 수정할 곳                조건 수정할 곳
#        (forecastData, Rainpercent, Wind)




# 	now = datetime.now()
# 	date = now.date()-relativedelta(days=x)


# 절대경로
abspath = os.path.dirname(os.path.abspath(__file__)) 
abspath = abspath.replace('\\','/')
abspath = abspath+'/static/graphs/'


#데이터 리스트
#forecastData(기온) 리스트
#{'id','fcstDate','fcstTime','fcstValue', 'fnx', 'fny','지역명'} 순서

def Forecast_chart():
    temps=[float(i[3]) for i in forecastData.objects.filter(fcstDate='20240417').values_list()]

    # temps = np.random.randint(14,20, size=24)
    # yesterday_temps = np.random.randint(17, 23, size=24)
    now = time

    plt.plot(range(len(temps)), temps, color='red', marker='o', linestyle='solid', label='today')
    # plt.plot(range(len(yesterday_temps)), yesterday_temps, color='red', linestyle=":", label='yesterday')
    plt.vlines(now.localtime().tm_hour, 0, 40, color='gray', linestyle='solid')

    plt.legend(loc='lower left', ncols=1)

    # plt.ylim(min(min(temps),min(yesterday_temps))-2 , max(max(temps),max(yesterday_temps))+2)
    plt.ylabel("Temperatures (°C)")
    plt.xlabel("Time (h)")

    #절대경로 +'파일이름'
    plt.savefig(abspath+'temp_graph.png', format='png')

#plt.rcParams['font.family'] ='Malgun Gothic'
#plt.rcParams['axes.unicode_minus'] =False

#index_num 추가예정
def charts():
    fig, axs = plt.subplots(1, 3, figsize=(20, 5))
    # plt.subplots_adjust(wspace = 0.15, hspace = 0.15)
    # data = [float(i[3]) for i in forecastData.objects.filter(fcstDate='20240417').values_list()]
    # date, time = date_to_str(0)
    # date_1day_ago, _ = date_to_str(1)
    # date_2day_ago, _ = date_to_str(2)
    # date_7day_ago, _ = date_to_str(7)
    
    # t = int(time)
    # time_range = list(range(t-2, t+6))
    # time_range = [x if x<24 else x-24 for x in time_range] # 24 이상이면 0부터
    # time_range = [x if x>=0 else x+24 for x in time_range] # 0 미만이면 23부터
    # time_range = [str(x) if len(str(x))==2 else '0'+str(x) for x in time_range] # 문자열화
    

    #{'id','fcstDate','fcstTime','fcstValue', 'fnx', 'fny','지역명'} 순서

    t =datetime.date.today()
    today = t.strftime("%Y%m%d")
    day_1_ago = (t - timedelta(days=1)).strftime("%Y%m%d")
    day_2_ago = (t - timedelta(days=2)).strftime("%Y%m%d")
    day_7_ago = (t - timedelta(days=7)).strftime("%Y%m%d")
    day = [today, day_1_ago, day_2_ago, day_7_ago]

    #시간 수정예정
    time_range = [i for i in range(0,24)]
    # 기온
    

    #index_num 받아와서 수정할 예정
    num = '156'
    temps_today = [float(i[3]) for i in forecastData.objects.filter(fcstDate=today, index_num= num).values_list()]
    temps_1day_ago = [float(i[3]) for i in forecastData.objects.filter(fcstDate=day_1_ago, index_num=num).values_list()]
    temps_2day_ago = [float(i[3]) for i in forecastData.objects.filter(fcstDate=day_2_ago, index_num=num).values_list()]
    temps_7day_ago = [float(i[3]) for i in forecastData.objects.filter(fcstDate=day_7_ago, index_num=num).values_list()]

    axs[0].set_title('Temperatures', fontsize = 12, fontweight ="bold")
    axs[0].plot([i for i in range(len(temps_today))], temps_today, color='red', marker='o', linestyle='solid', label='today')
    axs[0].plot([i for i in range(len(temps_1day_ago))], temps_1day_ago, color='black', linestyle=":", label='1 day ago')
    axs[0].plot([i for i in range(len(temps_2day_ago))], temps_2day_ago, color='gray', linestyle=":", label='2 day ago')
    axs[0].plot([i for i in range(len(temps_7day_ago))], temps_7day_ago, color='lightgray', linestyle=":", label='7 day ago')

    #시간, 값
    all_temps = temps_today+temps_1day_ago+temps_2day_ago+temps_7day_ago
    all_temps2 = [[float(i[2]),float(i[3])] for i in forecastData.objects.filter(fcstDate=day_1_ago, index_num=num).values_list()]
    all_temps2.sort(key=lambda x:x[1])

    #수직선 제일 작은 값, 큰 값
    axs[0].vlines(all_temps2[0][0], min(all_temps)-4, max(all_temps)+4, color='gray', linestyle='solid')
    axs[0].vlines(all_temps2[-1][0], min(all_temps)-4, max(all_temps)+4, color='gray', linestyle='solid')

    axs[0].legend(loc='upper left', ncols=1)
    axs[0].set_ylabel("Temperatures (°C)")
    axs[0].set_xlabel("Time (h)")
    axs[0].set_ylim(min(all_temps)-4, max(all_temps)+4)

    # #풍속
    wind_today = [float(i[3]) for i in Wind.objects.filter(fcstDate=today, index_num=num).values_list()]
    wind_1day_ago = [float(i[3]) for i in Wind.objects.filter(fcstDate=day_1_ago, index_num=num).values_list()]
    wind_2day_ago = [float(i[3]) for i in Wind.objects.filter(fcstDate=day_2_ago, index_num=num).values_list()]
    wind_7day_ago = [float(i[3]) for i in Wind.objects.filter(fcstDate=day_7_ago, index_num=num).values_list()]


    axs[1].set_title('Wind Speeds', fontsize = 12, fontweight ="bold")
    axs[1].plot([i for i in range(len(wind_today))], wind_today, color='green', marker='o', linestyle='solid', label='today')
    axs[1].plot([i for i in range(len(wind_1day_ago))], wind_1day_ago, color='black', linestyle=":", label='1 day ago')
    axs[1].plot([i for i in range(len(wind_2day_ago))], wind_2day_ago, color='gray', linestyle=":", label='2 day ago')
    axs[1].plot([i for i in range(len(wind_7day_ago))], wind_7day_ago, color='lightgray', linestyle=":", label='7 day ago')
    
    all_wind = wind_today+wind_1day_ago+wind_2day_ago+wind_7day_ago
    all_wind2 = [[float(i[2]),float(i[3])] for i in Wind.objects.filter(fcstDate=day_1_ago, index_num=num).values_list()]
    all_wind2.sort(key=lambda x:x[1])

    axs[1].vlines(all_wind2[0][0], min(all_wind)-4, max(all_wind)+4, color='gray', linestyle='solid')
    axs[1].vlines(all_wind2[-1][0], min(all_wind)-4, max(all_wind)+4, color='gray', linestyle='solid')



    axs[1].legend(loc='upper left', ncols=1)
    axs[1].set_ylabel("Wind Speeds (m/s)")
    axs[1].set_xlabel("Time (h)")
    axs[1].set_ylim(min(all_wind)-4, max(all_wind)+4)

    # #강수량
    rain_today = [float(i[3]) for i in Rainpercent.objects.filter(fcstDate=today, index_num=num).values_list()]
    rain_1day_ago = [float(i[3]) for i in Rainpercent.objects.filter(fcstDate=day_1_ago, index_num=num).values_list()]
    rain_2day_ago = [float(i[3]) for i in Rainpercent.objects.filter(fcstDate=day_2_ago, index_num=num).values_list()]
    rain_7day_ago = [float(i[3]) for i in Rainpercent.objects.filter(fcstDate=day_7_ago, index_num=num).values_list()]

    axs[2].set_title('Rainfalls', fontsize = 12, fontweight ="bold")
    axs[2].plot([i for i in range(len(rain_today))], rain_today, color='blue', marker='o', linestyle='solid', label='today')
    axs[2].plot([i for i in range(len(rain_1day_ago))], rain_1day_ago, color='black', linestyle=":", label='1 day ago')
    axs[2].plot([i for i in range(len(rain_2day_ago))], rain_2day_ago, color='gray', linestyle=":", label='2 day ago')
    axs[2].plot([i for i in range(len(rain_7day_ago))], rain_7day_ago, color='lightgray', linestyle=":", label='7 day ago')
    
    all_rain = rain_today+rain_1day_ago+rain_2day_ago+rain_7day_ago
    all_rain2 = [[float(i[2]),float(i[3])] for i in Rainpercent.objects.filter(fcstDate=day_1_ago, index_num=num).values_list()]
    all_rain2.sort(key=lambda x:x[1])

    axs[2].vlines(all_rain2[0][0], min(all_rain)-4, max(all_rain)+4, color='gray', linestyle='solid')
    axs[2].vlines(all_rain2[-1][0], min(all_rain)-4, max(all_rain)+4, color='gray', linestyle='solid')

    axs[2].legend(loc='upper left', ncols=1)
    axs[2].set_ylabel("Precipitation (mm)")
    axs[2].set_xlabel("Time (h)")
    axs[2].set_ylim(min(all_rain)-4, max(all_rain)+4)

    fig.tight_layout()
    plt.savefig(abspath+'all_graph.png', format='png')
    # plt.show()
