import requests
import pandas as pd
import numpy as np
from pyecharts.charts import Geo
from pyecharts import options as opts

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

bjdata = []
shdata = []
gzdata = []
szdata = []
cddata = []

data = [bjdata, shdata, gzdata, szdata, cddata]

#  删除 板块 为空的行
for i in range(0, 5):
    zufang[i] = zufang[i].dropna(axis=0, subset='板块')

# 获取每座城市的板块均价
for index in range(0, 5):
    city = zufang[index]
    curPlateName = city['板块'].unique().tolist()  # 获取每座城市的板块名
    plateName.append(curPlateName)
    plateList = []
    for k in range(0, len(curPlateName)):
        plateList.append([])
    for i in city.index.tolist():
        if '-' in str(city['租价（元/月）'][i]):
            zone = str(city['租价（元/月）'][i]).split('-')
            plateList[curPlateName.index(city['板块'][i])].append((eval(zone[0]) + eval(zone[1])) / 2)
        else:
            tmp = str(city['租价（元/月）'][i])
            plateList[curPlateName.index(city['板块'][i])].append(eval(tmp))
    for i in plateList:
        data[index].append(np.mean(i))

cityName = ['北京市', '上海市', '广州市', '深圳市', '常德市']

locations = [{}, {}, {}, {}, {}]
apiurl = 'http://api.map.baidu.com/geocoding/v3/?'
# 获取板块对应的经纬度信息
for index in range(0, 5):
    for name in plateName[index]:
        params = {
            'address': name,
            'city': cityName[index],
            'output': 'json',
            'ak': 'hbVOogf05TdAXcd67WCnyhpYf0yjVpv0'
        }
        res = requests.get(apiurl, params=params)
        answer = res.json()
        if answer['status'] == 0:
            tmpList = answer['result']
            coordString = tmpList['location']
            coordList = [coordString['lng'], coordString['lat']]
        print(name + ',' + str(float(coordList[0])) + ',' + str(float(coordList[1])))
        locations[index][name] = [float(coordList[0]), float(coordList[1])]

for index in range(0, 5):
    g = Geo()
    g.add_schema(maptype=cityName[index].strip('市'))
    for key, value in locations[index].items():
        g.add_coordinate(key, value[0], value[1])
    data_pair = [list(z) for z in zip(plateName[index], data[index])]
    g.add('总租价均价', data_pair, symbol_size=8)
    g.set_series_opts(label_opts=opts.LabelOpts(is_show=False))
    g.set_global_opts(visualmap_opts=opts.VisualMapOpts(max_=np.max(data[index])), title_opts=opts.TitleOpts(title=cityName[index] + '板块房租分布图'))
    g.render(path=cityName[index] + '板块房租分布图' + ".html")
