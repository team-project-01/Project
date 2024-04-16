#%%

import matplotlib.pyplot as plt
import random

plt.rcParams['font.family'] ='Malgun Gothic'
plt.rcParams['axes.unicode_minus'] =False

def line_graph():
#기온, 풍속, 강수량
#오늘 1일전 2일전 일주일전 - 
#24시간 1시간단위로 수정예정 - x축
    x = [i for i in range(0,24)]
    #기온
    a1 = random.sample(range(0,30),24)      
    a2 = random.sample(range(0,30),24)
    a3 = random.sample(range(0,30),24)
    a4 = random.sample(range(0,30),24)
    #풍속
    b1 = random.sample(range(0,30),24)      
    b2 = random.sample(range(0,30),24)
    b3 = random.sample(range(0,30),24)
    b4 = random.sample(range(0,30),24)
    #강수량
    c1 = random.sample(range(0,30),24)      
    c2 = random.sample(range(0,30),24)
    c3 = random.sample(range(0,30),24)
    c4 = random.sample(range(0,30),24)

    fig, axs = plt.subplots(3,1)
    # plt.subplots_adjust(wspace = 0.15, hspace = 0.15)

    fig.suptitle('Weather',fontweight ="bold", fontsize=20) 
    #기온
    axs[0].set_title('기온', fontsize = 12,fontweight ="bold")
    axs[0].plot(x, a1, label = '7일전', color = 'r')  
    axs[0].plot(x, a2, label = '2일전', color = 'g')  
    axs[0].plot(x, a3, label = '1일전', color = 'b')  
    axs[0].plot(x, a4, label = '오늘', color = 'y') 
    axs[0].set_xlim(0,23)  #x축시간 0~23시 까지
    fig.legend()

    #풍속
    axs[1].set_title('풍속', fontsize = 12,fontweight ="bold")
    axs[1].plot(x, b1, label = '7일전', color = 'r')  
    axs[1].plot(x, b2, label = '2일전', color = 'g')  
    axs[1].plot(x, b3, label = '1일전', color = 'b')  
    axs[1].plot(x, b4, label = '오늘', color = 'y')  
    axs[0].set_xlim(0,23) 

    #강수량
    axs[2].set_title('강수량', fontsize = 12,fontweight ="bold")
    axs[2].plot(x, c1, label = '7일전', color = 'r')  
    axs[2].plot(x, c2, label = '2일전', color = 'g')  
    axs[2].plot(x, c3, label = '1일전', color = 'b')  
    axs[2].plot(x, c4, label = '오늘', color = 'y')  
    fig.tight_layout()
    axs[0].set_xlim(0,23) 

    
    # plt.savefig('chart/line_chart.png')
    return plt.show()
print(line_graph())
# %%
