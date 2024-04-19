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
import numpy as np

#temps=[float(i[3]) for i in forecastData.objects.filter(fcstDate='20240417').values_list()]
#                    단위값 수정할 곳                조건 수정할 곳
#        (forecastData, Rainpercent, Wind)

# 절대경로
abspath = os.path.dirname(os.path.abspath(__file__)) 
abspath = abspath.replace('\\','/')
abspath = abspath+'/static/graphs/'


t =datetime.date.today()
today = t.strftime("%Y%m%d")
day_1_ago = (t - timedelta(days=1)).strftime("%Y%m%d")
day_2_ago = (t - timedelta(days=2)).strftime("%Y%m%d")
day_7_ago = (t - timedelta(days=7)).strftime("%Y%m%d")

#한글 고딕체
#plt.rcParams['font.family'] ='Malgun Gothic'
#plt.rcParams['axes.unicode_minus'] =False

def charts(area2):
    num = area2
    fig, axs = plt.subplots(1, 3, figsize=(20, 5))

    #{'id','fcstDate','fcstTime','fcstValue', 'fnx', 'fny','지역명'} 순서
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
    temps1 = [[float(i[2]),float(i[3])] for i in forecastData.objects.filter(fcstDate=today, index_num=num).values_list()]
    temps2 = [[float(i[2]),float(i[3])] for i in forecastData.objects.filter(fcstDate=day_1_ago, index_num=num).values_list()]
    temps3 = [[float(i[2]),float(i[3])] for i in forecastData.objects.filter(fcstDate=day_2_ago, index_num=num).values_list()]
    temps4 = [[float(i[2]),float(i[3])] for i in forecastData.objects.filter(fcstDate=day_7_ago, index_num=num).values_list()]
    all_temps2 = temps1+temps2+temps3+temps4
    all_temps2.sort(key=lambda x:x[1])

    #수직선 모든 값들(7일전~오늘)중 제일 작은 값, 큰 값
    axs[0].vlines(all_temps2[0][0], min(all_temps)-4, max(all_temps)+4, color='gray', linestyle='solid')
    axs[0].vlines(all_temps2[-1][0], min(all_temps)-4, max(all_temps)+4, color='gray', linestyle='solid')

    axs[0].legend(loc='upper left', ncols=1)
    axs[0].set_ylabel("Temperatures (°C)")
    axs[0].set_xlabel("Time (h)")
    axs[0].set_ylim(min(all_temps)-4, max(all_temps)+4)
    axs[0].set_xlim(0, 23)
    plt.setp(axs[0], xticks=[3,6,9,12,15,18,21])
    
    
    #풍속
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
    wind1 = [[float(i[2]),float(i[3])] for i in Wind.objects.filter(fcstDate=today, index_num=num).values_list()]
    wind2 = [[float(i[2]),float(i[3])] for i in Wind.objects.filter(fcstDate=day_1_ago, index_num=num).values_list()]
    wind3 = [[float(i[2]),float(i[3])] for i in Wind.objects.filter(fcstDate=day_2_ago, index_num=num).values_list()]
    wind4 = [[float(i[2]),float(i[3])] for i in Wind.objects.filter(fcstDate=day_7_ago, index_num=num).values_list()]
    all_wind2 = wind1+wind2+wind3+wind4
    all_wind2.sort(key=lambda x:x[1])

    axs[1].vlines(all_wind2[0][0], min(all_wind)-4, max(all_wind)+4, color='gray', linestyle='solid')
    axs[1].vlines(all_wind2[-1][0], min(all_wind)-4, max(all_wind)+4, color='gray', linestyle='solid')

    axs[1].legend(loc='upper left', ncols=1)
    axs[1].set_ylabel("Wind Speeds (m/s)")
    axs[1].set_xlabel("Time (h)")
    axs[1].set_ylim(-1, max(all_wind)+4)
    axs[1].set_xlim(0, 23)
    plt.setp(axs[1], xticks=[3,6,9,12,15,18,21])
    wind_yticks = [i for i in range(-1,int(max(all_wind)+4),int((max(all_wind)+4)/((max(all_wind)+4)/2)))]
    plt.setp(axs[1], yticks=[-1,0]+wind_yticks)

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
    rain1 = [[float(i[2]),float(i[3])] for i in Rainpercent.objects.filter(fcstDate=today, index_num=num).values_list()]
    rain2 = [[float(i[2]),float(i[3])] for i in Rainpercent.objects.filter(fcstDate=day_1_ago, index_num=num).values_list()]
    rain3 = [[float(i[2]),float(i[3])] for i in Rainpercent.objects.filter(fcstDate=day_2_ago, index_num=num).values_list()]
    rain4 = [[float(i[2]),float(i[3])] for i in Rainpercent.objects.filter(fcstDate=day_7_ago, index_num=num).values_list()]
    all_rain2 = rain1+rain2+rain3+rain4
    all_rain2.sort(key=lambda x:x[1])

    axs[2].vlines(all_rain2[0][0], min(all_rain)-4, max(all_rain)+4, color='gray', linestyle='solid')
    axs[2].vlines(all_rain2[-1][0], min(all_rain)-4, max(all_rain)+4, color='gray', linestyle='solid')

    axs[2].legend(loc='upper left', ncols=1)
    axs[2].set_ylabel("Precipitation (mm)")
    axs[2].set_xlabel("Time (h)")
    axs[2].set_ylim(-1, max(all_rain)+4)
    axs[2].set_xlim(0, 23)
    plt.setp(axs[2], xticks=[3,6,9,12,15,18,21])
    rain_yticks = [i for i in range(-1,int(max(all_rain)+4),int((max(all_rain)+4)/((max(all_rain)+4)/2)))]
    plt.setp(axs[2], yticks=[-1,0]+rain_yticks)

    fig.tight_layout()
    plt.savefig(abspath+'all_graph.png', format='png')



    def min_max_temps(num) :
        num = area2

        temps_today = [float(i[3]) for i in forecastData.objects.filter(fcstDate=today, index_num= num).values_list()]
        temps_1day_ago = [float(i[3]) for i in forecastData.objects.filter(fcstDate=day_1_ago, index_num=num).values_list()]
        temps_2day_ago = [float(i[3]) for i in forecastData.objects.filter(fcstDate=day_2_ago, index_num=num).values_list()]
        temps_7day_ago = [float(i[3]) for i in forecastData.objects.filter(fcstDate=day_7_ago, index_num=num).values_list()]

        all_temps = temps_today+temps_1day_ago+temps_2day_ago+temps_7day_ago
        
        return [min(all_temps), max(all_temps)]

    def min_max_wind(num) :
        num = area2

        wind_today = [float(i[3]) for i in Wind.objects.filter(fcstDate=today, index_num=num).values_list()]
        wind_1day_ago = [float(i[3]) for i in Wind.objects.filter(fcstDate=day_1_ago, index_num=num).values_list()]
        wind_2day_ago = [float(i[3]) for i in Wind.objects.filter(fcstDate=day_2_ago, index_num=num).values_list()]
        wind_7day_ago = [float(i[3]) for i in Wind.objects.filter(fcstDate=day_7_ago, index_num=num).values_list()]

        all_wind = wind_today+wind_1day_ago+wind_2day_ago+wind_7day_ago
        return [min(all_wind),max(all_wind)]
    
    def min_max_rain(num) :
        num = area2
        
        rain_today = [float(i[3]) for i in Rainpercent.objects.filter(fcstDate=today, index_num=num).values_list()]
        rain_1day_ago = [float(i[3]) for i in Rainpercent.objects.filter(fcstDate=day_1_ago, index_num=num).values_list()]
        rain_2day_ago = [float(i[3]) for i in Rainpercent.objects.filter(fcstDate=day_2_ago, index_num=num).values_list()]
        rain_7day_ago = [float(i[3]) for i in Rainpercent.objects.filter(fcstDate=day_7_ago, index_num=num).values_list()]

        all_rain = rain_today+rain_1day_ago+rain_2day_ago+rain_7day_ago

        return [min(all_rain), max(all_rain)]



    # plt.show()
