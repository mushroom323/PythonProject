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

# 总

# 均价
average = []
for city in zufang:
    average.append(city['租价（元/月）'].mean())

highest = []
for city in zufang:
    highest.append(city['租价（元/月）'].max())

lowest = []
for city in zufang:
    lowest.append(city['租价（元/月）'].min())

medium = []
for city in zufang:
    medium.append(city['租价（元/月）'].median())

# 平均
unitData = []
for city in zufang:
    pricecopy = city['租价（元/月）'].copy()
    for i in range(0, len(pricecopy)):
        pricecopy[i] = pricecopy[i] / city['面积（㎡）'][i]
    unitData.append(pricecopy)

unitAverage = []
for city in unitData:
    unitAverage.append(city.mean())

unitHigh = []
for city in unitData:
    unitHigh.append(city.max())

unitLow = []
for city in unitData:
    unitLow.append(city.min())

unitmeidum = []
for city in unitData:
    unitmeidum.append(city.median())


def plot(data, labels, visualName):
    plt.rcParams['font.sans-serif'] = ['SimHei']  # 显示中文
    width = 0.15
    plt.figure(figsize=(10, 10))
    plt.ylabel('租金', fontsize=12)
    plt.title(visualName)
    plt.ticklabel_format(style='plain')
    x = np.arange(len(labels))
    plt.xticks(x, labels=labels)
    plt.bar(x - 2*width, data[0], width=width, color='darkorange')
    plt.bar(x - width, data[1], width=width, color='deepskyblue')
    plt.bar(x, data[2], width=width, color='g')
    plt.bar(x + width, data[3], width=width, color='y')
    plt.bar(x + 2*width, data[4], width=width, color='cyan')

    for cdata in range(0, 5):
        for a, b in zip(x, data[cdata]):
            plt.text(a + (cdata - 2) * width, b, "{:.2f}".format(b), ha='center', va='bottom', fontsize=8)

    plt.legend(['北京', '上海', '广州', '深圳', '常德'])
    plt.savefig(visualName + '.png')
    plt.show()


bjdata = []
shdata = []
gzdata = []
szdata = []
cddata = []

data = [bjdata, shdata, gzdata, szdata, cddata]

# 总价： 均价 最低价 中位数
for i in range(0, 5):
    data[i].append(average[i])
    # data[i].append(highest[i])
    data[i].append(lowest[i])
    data[i].append(medium[i])

plot(data, ['均价', '最低价', '中位数'], '总体房租情况（总价）')

# 总价 最高价

bjdata = []
shdata = []
gzdata = []
szdata = []
cddata = []

data = [bjdata, shdata, gzdata, szdata, cddata]

for i in range(0, 5):
    data[i].append(highest[i])

plot(data, ['最高价'], '总体房租情况（总价最高价）')

# 平均价 均价 最低价 中位数

bjdata = []
shdata = []
gzdata = []
szdata = []
cddata = []

data = [bjdata, shdata, gzdata, szdata, cddata]

for i in range(0, 5):
    data[i].append(unitAverage[i])
    # data[i].append(unitHigh[i])
    data[i].append(unitLow[i])
    data[i].append(unitmeidum[i])

plot(data, ['均价', '最低价', '中位数'], '总体房租情况（均价）')


# 平均价 最高价

bjdata = []
shdata = []
gzdata = []
szdata = []
cddata = []

data = [bjdata, shdata, gzdata, szdata, cddata]

for i in range(0, 5):
    data[i].append(unitHigh[i])

plot(data, ['最高价'], '总体房租情况（均价最高价）')

