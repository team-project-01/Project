#%%
import matplotlib.pyplot as plt
import numpy as np
#from django.utils import timezone
import time
from datetime import datetime
from dateutil.relativedelta import relativedelta
from .models import *
import os

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

def charts():
    fig, axs = plt.subplots(1, 3, figsize=(20, 5))
    # plt.subplots_adjust(wspace = 0.15, hspace = 0.15)

    date, time = date_to_str(0)
    date_1day_ago, _ = date_to_str(1)
    date_2day_ago, _ = date_to_str(2)
    date_7day_ago, _ = date_to_str(7)
    
    t = int(time)
    time_range = list(range(t-2, t+6))
    time_range = [x if x<24 else x-24 for x in time_range] # 24 이상이면 0부터
    time_range = [x if x>=0 else x+24 for x in time_range] # 0 미만이면 23부터
    time_range = [str(x) if len(str(x))==2 else '0'+str(x) for x in time_range] # 문자열화

    # 기온
    temps = list(np.random.randint(14, 20, size=8))
    temps_1day_ago = list(np.random.randint(17, 23, size=8))
    temps_2day_ago = list(np.random.randint(17, 23, size=8))
    temps_7day_ago = list(np.random.randint(17, 23, size=8))

    axs[0].set_title('Temperatures', fontsize = 12, fontweight ="bold")
    axs[0].plot(time_range, temps, color='red', marker='o', linestyle='solid', label='today')
    axs[0].plot(time_range, temps_1day_ago, color='black', linestyle=":", label='1 day ago')
    axs[0].plot(time_range, temps_2day_ago, color='gray', linestyle=":", label='2 day ago')
    axs[0].plot(time_range, temps_7day_ago, color='lightgray', linestyle=":", label='7 day ago')
    axs[0].vlines(time, 0, 40, color='gray', linestyle='solid')

    axs[0].legend(loc='upper left', ncols=1)
    axs[0].set_ylabel("Temperatures (°C)")
    axs[0].set_xlabel("Time (h)")
    all_temps = temps+temps_1day_ago+temps_2day_ago+temps_7day_ago
    axs[0].set_ylim(min(all_temps)-4, max(all_temps)+4)

    #풍속
    winds = list(np.random.randint(14, 20, size=8))
    winds_1day_ago = list(np.random.randint(17, 23, size=8))
    winds_2day_ago = list(np.random.randint(17, 23, size=8))
    winds_7day_ago = list(np.random.randint(17, 23, size=8))

    axs[1].set_title('Wind Speeds', fontsize = 12, fontweight ="bold")
    axs[1].plot(time_range, winds, color='green', marker='o', linestyle='solid', label='today')
    axs[1].plot(time_range, winds_1day_ago, color='black', linestyle=":", label='1 day ago')
    axs[1].plot(time_range, winds_2day_ago, color='gray', linestyle=":", label='2 day ago')
    axs[1].plot(time_range, winds_7day_ago, color='lightgray', linestyle=":", label='7 day ago')
    axs[1].vlines(time, 0, 40, color='gray', linestyle='solid')

    axs[1].legend(loc='upper left', ncols=1)
    axs[1].set_ylabel("Wind Speeds (m/s)")
    axs[1].set_xlabel("Time (h)")
    all_winds = winds+winds_1day_ago+winds_2day_ago+winds_7day_ago
    axs[1].set_ylim(min(all_winds)-4, max(all_winds)+4)

    #강수량
    rainf = list(np.random.randint(14, 20, size=8))
    rainf_1day_ago = list(np.random.randint(17, 23, size=8))
    rainf_2day_ago = list(np.random.randint(17, 23, size=8))
    rainf_7day_ago = list(np.random.randint(17, 23, size=8))

    axs[2].set_title('Rainfalls', fontsize = 12, fontweight ="bold")
    axs[2].plot(time_range, rainf, color='blue', marker='o', linestyle='solid', label='today')
    axs[2].plot(time_range, rainf_1day_ago, color='black', linestyle=":", label='1 day ago')
    axs[2].plot(time_range, rainf_2day_ago, color='gray', linestyle=":", label='2 day ago')
    axs[2].plot(time_range, rainf_7day_ago, color='lightgray', linestyle=":", label='7 day ago')
    axs[2].vlines(time, 0, 40, color='gray', linestyle='solid')

    axs[2].legend(loc='upper left', ncols=1)
    axs[2].set_ylabel("Precipitation (mm)")
    axs[2].set_xlabel("Time (h)")
    all_rainf = rainf+rainf_1day_ago+rainf_2day_ago+rainf_7day_ago
    axs[2].set_ylim(min(all_rainf)-4, max(all_rainf)+4)

    fig.tight_layout()
#    plt.savefig('static/graphs/graph.png', format='png')
    plt.show()
