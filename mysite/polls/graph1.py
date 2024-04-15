#%%

import matplotlib.pyplot as plt
plt.rcParams['font.family'] ='Malgun Gothic'
plt.rcParams['axes.unicode_minus'] =False
#기온, 풍속, 강수량
#오늘 1일전 2일전 일주일전
x = ['7일전','2일','1일전','오늘']
a1 = [10,20,50,20]         
a2 = [30,20,40,10]
a3 = [30,20,10,40]    

fig, axs = plt.subplots(1,3)

fig.suptitle('Weather',fontweight ="bold", fontsize=20) 

axs[0].plot(x, a1, label = '기온', color = 'r')  
axs[0].legend()
axs[0].set_ylim(5,65)

axs[1].plot(x, a2, label = '풍속', color = 'g')
axs[1].legend()

axs[2].plot(x, a3, label = '강수량', color = 'b')
axs[2].legend()
fig.tight_layout()

plt.show()
# %%
