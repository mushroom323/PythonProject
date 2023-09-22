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

# 平均
unitData = []
for city in zufang:
    pricecopy = city['租价（元/月）'].copy()
    for i in range(0, len(pricecopy)):
        pricecopy[i] = pricecopy[i] / city['面积（㎡）'][i]
    unitData.append(pricecopy)

data = []
for index in unitData:
    data.append(np.mean(index))

aveGdp = [183937.45, 173756.71, 151162.22, 174628.38, 76796.23]
aveWage = [35549, 35487, 31421, 31889, 7270]

que = [aveGdp, aveWage]

plt.rcParams['font.sans-serif'] = ['SimHei']  # 显示中文

queName = ['人均GDP（元/年）', '人均工资（元/月）']

for ques in range(0, 2):
    width = 0.3
    labels = ['北京', '上海', '广州', '深圳', '常德']
    x = np.arange(len(labels))

    # 创建图层
    fig, ax1 = plt.subplots(figsize=(16, 16))

    # 绘制柱形图1
    b1 = ax1.bar(x, data, width=width, label='平均单位面积租金（元/平米）', color='g', tick_label=labels)

    # 绘制柱形图2---双Y轴
    ax2 = ax1.twinx()
    b2 = ax2.bar(x + width, que[ques], width=width, label=queName[ques], color='y')

    # 坐标轴标签设置
    ax1.set_title('总体房租情况（均价）与' + queName[ques] + '关系展示', fontsize=14)
    ax1.set_xlabel('城市', fontsize=12)
    ax1.set_ylabel('平均单位面积租金（元/平米）', fontsize=12)
    ax2.set_ylabel(queName[ques], fontsize=12)

    # x轴标签旋转
    ax1.set_xticklabels(ax1.get_xticklabels(), rotation=25)

    for a, b in zip(x, data):
        ax1.text(a, b, "{:.2f}".format(b), ha='center', va='bottom', fontsize=8)
    
    for a, b in zip(x, que[ques]):
        ax2.text(a + width, b, "{:.2f}".format(b), ha='center', va='bottom', fontsize=8)

    plt.legend(handles=[b1, b2])
    plt.savefig('ques_' + str(ques) + '.png')
    plt.show()