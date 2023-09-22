import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)
pd.set_option('display.float_format', lambda x: '%.4f' % x)
beijing = pd.read_csv('beijing.csv', sep=',', encoding="utf-8")
shanghai = pd.read_csv('shanghai.csv', sep=',', encoding="utf-8")
guangzhou = pd.read_csv('guangzhou.csv', sep=',', encoding="utf-8")
shenzhen = pd.read_csv('shenzhen.csv', sep=',', encoding="utf-8")
changde = pd.read_csv('changde.csv', sep=',', encoding="utf-8")

zufang = [beijing, shanghai, guangzhou, shenzhen, changde]

plateName = []

bjdata = [[], [], []]
shdata = [[], [], []]
gzdata = [[], [], []]
szdata = [[], [], []]
cddata = [[], [], []]

data = [bjdata, shdata, gzdata, szdata, cddata]

# 处理价格区间
for city in zufang:
    pricecopy = city['租价（元/月）']
    for i in range(0, len(city['租价（元/月）'])):
        if '-' in str(city['租价（元/月）'][i]):
            zone = str(city['租价（元/月）'][i]).split('-')
            pricecopy[i] = (eval(zone[0]) + eval(zone[1])) / 2
    city['租价（元/月）'] = pricecopy
    city['租价（元/月）'] = city['租价（元/月）'].astype(float)

# 处理面积区间
for city in zufang:
    areacopy = city['面积（㎡）'].copy()
    for i in range(0, len(city['面积（㎡）'])):
        if '-' in str(city['面积（㎡）'][i]):
            zone = str(city['面积（㎡）'][i]).split('-')
            areacopy[i] = (eval(zone[0]) + eval(zone[1])) / 2
    city['面积（㎡）'] = areacopy
    city['面积（㎡）'] = city['面积（㎡）'].astype(float)

#  删除 朝向 为空的行
for i in range(0, 5):
    zufang[i] = zufang[i].dropna(subset=["朝向"])

print('Get over.')
# 获取每座城市的朝向均价
toMap = {'东': 0, '东南': 1, '南': 2, '西南': 3, '西': 4, '西北': 5, '北': 6, '东北': 7}
for index in range(0, 5):
    city = zufang[index]
    towardList = []
    for k in range(0, 8):  # 东 东南 南 西南 西 西北 北 东北 东南
        towardList.append([])
    for i in city.index.tolist():
        tos = city['朝向'][i].split()
        for to in tos:
            towardList[toMap[to]].append(city['租价（元/月）'][i] / city['面积（㎡）'][i])
    for i in towardList:
        if len(i) != 0:
            data[index][0].append(np.max(i))
            data[index][1].append(np.min(i))
            data[index][2].append(np.mean(i))
        else:
            data[index][0].append(0)
            data[index][1].append(0)
            data[index][2].append(0)

print('Process over.')

plt.rcParams['font.sans-serif'] = ['SimHei']  # 显示中文

cityName = ['北京', '上海', '广州', '深圳', '常德']
toName = ['东', '东南', '南', '西南', '西', '西北', '北', '东北']
information = ['最高价', '最低价', '均价']
for i in range(0, 5):
    plt.xlabel('朝向')
    plt.ylabel('平均单位面积租金（元/平米）')
    colors = ['.r-', '.b-', '.g-']
    lines = []
    for index in range(0, 3):
        p, = plt.plot(toName, data[i][index], colors[index])
        for a, b in zip(toName, data[i][index]):
            plt.text(a, b, "{:.2f}".format(b), ha='center', va='bottom', fontsize=8)
        lines.append(p)
    plt.legend(lines, information, loc='upper right')
    plt.grid(linestyle='--')
    plt.tick_params(axis='y', direction='in', color='r', grid_color='r')
    plt.title(cityName[i] + '朝向分析图')
    plt.savefig('towards_' + str(i) + '.png')
    plt.show()