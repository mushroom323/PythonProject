# 导入 requests 包
import requests
import csv
import parsel
import time

f1 = open('东城.csv', mode='x', encoding='utf-8-sig', newline='')
f2 = open('西城.csv', mode='x', encoding='utf-8-sig', newline='')
f3 = open('朝阳.csv', mode='x', encoding='utf-8-sig', newline='')
f4 = open('海淀.csv', mode='x', encoding='utf-8-sig', newline='')
csv_writer1 = csv.DictWriter(f1, fieldnames=['楼盘名称', '平米数', '总价', '单价'])
csv_writer1.writeheader()
csv_writer2 = csv.DictWriter(f2, fieldnames=['楼盘名称', '平米数', '总价', '单价'])
csv_writer2.writeheader()
csv_writer3 = csv.DictWriter(f3, fieldnames=['楼盘名称', '平米数', '总价', '单价'])
csv_writer3.writeheader()
csv_writer4 = csv.DictWriter(f4, fieldnames=['楼盘名称', '平米数', '总价', '单价'])
csv_writer4.writeheader()

csv_writers = [csv_writer1, csv_writer2, csv_writer3, csv_writer4]
zoneList = ["dongcheng", "xicheng", "chaoyang", "haidian"]
for i in range(4):
    time.sleep(1)
    for page in range(1, 6):
        url = 'https://bj.lianjia.com/ershoufang/' + zoneList[i] + '/pg' + str(page) + '/'
        headers = {
            'User-Agent':
            'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36'
        }
        response = requests.get(url=url, headers=headers)
        selector = parsel.Selector(response.text)
        lis = selector.css('.sellListContent li')
        dit = {}
        for li in lis:
            title = li.css('.title a::text').get()
            dit['楼盘名称'] = title
            houseInfo = li.css('.houseInfo::text').get().split("|")[1].strip()
            dit['平米数'] = houseInfo
            Price = str(li.css('.totalPrice span::text').get()) + "万"
            dit['总价'] = Price
            unitPrice = li.css('.unitPrice span::text').get()
            dit['单价'] = unitPrice
            csv_writers[i].writerow(dit)