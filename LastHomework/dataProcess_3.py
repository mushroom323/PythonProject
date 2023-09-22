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

bjData = []
shData = []
gzData = []
szData = []
cdData = []
Data = [bjData, shData, gzData, szData, cdData]
for index in range(0, 5):
    city = zufang[index]
    room = city['房型'].copy()
    price = city['租价（元/月）'].copy()
    price1 = []
    price2 = []
    price3 = []
    for i in range(0, len(city)):
        if '1室' in str(city['房型'][i]): 
            if '-' in str(city['租价（元/月）'][i]):
                zone = str(city['租价（元/月）'][i]).split('-')
                price1.append((eval(zone[0]) + eval(zone[1])) / 2)
            else:
                tmp = str(city['租价（元/月）'][i])
                price1.append(eval(tmp))
        elif '2室' in str(city['房型'][i]):
            if '-' in str(city['租价（元/月）'][i]):
                zone = str(city['租价（元/月）'][i]).split('-')
                price2.append((eval(zone[0]) + eval(zone[1])) / 2)
            else:
                tmp = str(city['租价（元/月）'][i])
                price2.append(eval(tmp))
        elif '3室' in str(city['房型'][i]):
            if '-' in str(city['租价（元/月）'][i]):
                zone = str(city['租价（元/月）'][i]).split('-')
                price3.append((eval(zone[0]) + eval(zone[1])) / 2)
            else:
                tmp = str(city['租价（元/月）'][i])
                price3.append(eval(tmp))
    Data[index].append(price1)
    Data[index].append(price2)
    Data[index].append(price3)


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
            plt.text(a + (cdata - 2) * width, b, "{:.2f}".format(b), ha='center', va='bottom', fontsize=6)

    plt.legend(['北京', '上海', '广州', '深圳', '常德'])
    plt.savefig(visualName + '.png')
    plt.show()


roomLabels = ['一居', '二居', '三居']
for jushi in range(0, 3):
    bjdata = []
    shdata = []
    gzdata = []
    szdata = []
    cddata = []

    data = [bjdata, shdata, gzdata, szdata, cddata]

    # 均价 最低价 中位数
    for i in range(0, 5):
        data[i].append(np.mean(Data[i][jushi]))
        data[i].append(np.max(Data[i][jushi]))
        data[i].append(np.min(Data[i][jushi]))
        data[i].append(np.median(Data[i][jushi]))
    plot(data, ['均价', '最高价', '最低价', '中位数'], roomLabels[jushi])