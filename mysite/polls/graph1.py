#%%

import matplotlib.pyplot as plt
plt.rcParams['font.family'] ='Malgun Gothic'
plt.rcParams['axes.unicode_minus'] =False
#기온-x, 풍속-y, 강수량-z 

x = [10,20,30,40,50,60,70,80]         
y = [30,40,60,20,10,40,20,70]
z = [20,40,50,80,60,90,10,20]    

plt.xlabel('연간')         
plt.ylabel('온도')          
plt.title('그래프')   
plt.plot(x, x, label = '기온')   
plt.plot(x, y, label = '풍속')
plt.plot(x, z, label = '강수량')

plt.legend()                   
plt.show()
# %%
