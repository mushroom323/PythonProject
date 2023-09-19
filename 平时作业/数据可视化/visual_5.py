import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

months = ['一月', '二月', '三月', '四月', '五月', '六月', '七月', '八月', '九月', '十月', '十一月', '十二月']
years = ['2010年', '2011年', '2012年', '2013年', '2014年', '2015年']
df = pd.read_csv('BeijingPM20100101_20151231.csv')

plt.figure(figsize=(15, 10))

matrix = np.zeros((6, 12))
plt.rcParams['font.sans-serif'] = ['SimHei']  # 显示中文
# 获取每年每月的 PM 平均数
for year in range(2010, 2016):
    for month in range(1, 13):
        x = year - 2010
        y = month - 1
        year_mask = df['year'] == year
        month_mask = df['month'] == month
        mask = year_mask & month_mask
        data = df.loc[mask]
        a = []
        if not np.isnan(data['PM_Dongsi'].mean()):
            a.append(data['PM_Dongsi'].mean())
        if not np.isnan(data['PM_Nongzhanguan'].mean()):
            a.append(data['PM_Nongzhanguan'].mean())
        if not np.isnan(data['PM_Dongsihuan'].mean()):
            a.append(data['PM_Dongsihuan'].mean())
        if not np.isnan(data['PM_US Post'].mean()):
            a.append(data['PM_US Post'].mean())
        ave = np.mean(a)
        matrix[x][y] = ave

plt.xlabel('月份')
plt.ylabel('PM (ug/m^3)')
colors = ['.r-', ',y--', 'oc-.', '^g:', '1m-', 'sb--']
lines = []
for i in range(6):
    p, = plt.plot(months, matrix[i], colors[i])
    lines.append(p)
plt.legend(lines, years, loc='upper right')
plt.grid(linestyle='--')
plt.tick_params(axis='y', direction='in', color='r', grid_color='r')
plt.savefig('visual_5.png')
plt.show()
