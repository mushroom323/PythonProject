import requests

apiurl = 'http://api.map.baidu.com/geocoding/v3/?'

name = '西山'

params = {
    'address': '西山',
    'city': '北京市',
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