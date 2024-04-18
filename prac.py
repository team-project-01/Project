#%%
import datetime
from datetime import timedelta

t =datetime.date.today()
today = t.strftime("%Y%m%d")
day_1_ago = (t - timedelta(days=1)).strftime("%Y%m%d")
day_2_ago = (t - timedelta(days=2)).strftime("%Y%m%d")
day_7_ago = (t - timedelta(days=7)).strftime("%Y%m%d")
print(t)
print(today)
print(day_1_ago)
print(day_7_ago)
print(day_2_ago)
# %%
import time
# t = 0
# time_range = list(range(t-2, t+6))
# time_range = [x if x<24 else x-24 for x in time_range] # 24 이상이면 0부터
# time_range = [x if x>=0 else x+24 for x in time_range] # 0 미만이면 23부터
# time_range = [str(x) if len(str(x))==2 else '0'+str(x) for x in time_range] # 문자열화
time_range = [i for i in range(0,24)]
print(time_range)
print(len(time_range))

    
# %%
