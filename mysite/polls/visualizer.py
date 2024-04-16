import matplotlib.pyplot as plt
import numpy as np
#from django.utils import timezone
import time

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

def temperature():
    temps = np.random.randint(14,20, size=24)
    yesterday_temps = np.random.randint(17, 23, size=24)
    now = time

    plt.plot(range(0, 24), temps, color='red', marker='o', linestyle='solid', label='today')
    plt.plot(range(0, 24), yesterday_temps, color='red', linestyle=":", label='yesterday')
    plt.vlines(now.localtime().tm_hour, 0, 40, color='gray', linestyle='solid')

    plt.legend(loc='lower left', ncols=1)
    min(temps)<min(yesterday_temps)
    plt.ylim(min(temps)-2 , max(temps)+2)
    plt.ylabel("Temperatures (°C)")
    plt.xlabel("Time (h)")

    plt.savefig('graphs\temp_graph.png', format='png')


def rainfall():
    rainf = np.random.randint(0,4, size=24)
    yesterday_rainf = np.random.randint(0, 2, size=24)
    now = time

    plt.plot(range(0, 24), rainf, color='blue', marker='o', linestyle='solid', label='today')
    plt.plot(range(0, 24), yesterday_rainf, color='blue', linestyle=":", label='yesterday')
    plt.vlines(now.localtime().tm_hour, 0, 40, color='gray', linestyle='solid')

    plt.legend(loc='upper left', ncols=1)
    plt.ylim(0, max(rainf) if max(rainf)>8 else 8)
    plt.ylabel("Rainfalls (mm)")
    plt.xlabel("Time (h)")

    plt.savefig('graphs\rain_graph.png', format='png')

def windspeed():
    winds = np.random.randint(1, 7, size=24)
    yesterday_winds = np.random.randint(1, 5, size=24)
    now = time

    plt.plot(range(0, 24), winds, color='green', marker='o', linestyle='solid', label='today')
    plt.plot(range(0, 24), yesterday_winds, color='green', linestyle=":", label='yesterday')
    plt.vlines(now.localtime().tm_hour, 0, 40, color='gray', linestyle='solid')

    plt.legend(loc='upper left', ncols=1)
    plt.ylim(0, max(winds) if max(winds)>15 else 15)
    plt.ylabel("Wind Speeds (m/s)")
    plt.xlabel("Time (h)")

    plt.savefig('graphs\wind_graph.png', format='png')

