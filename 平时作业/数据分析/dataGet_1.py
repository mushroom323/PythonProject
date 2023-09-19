import requests
import csv
import parsel
import time

f1 = open('loupan.csv', mode='x', encoding='utf-8', newline='')
csv_writer1 = csv.DictWriter(f1, fieldnames=['名称', '地理位置（字段1）', '地理位置（字段2）', '地理位置（字段3）', '房型', '面积（㎡）', '均价（元/平米）', '总价（万元/套）'])
csv_writer1.writeheader()

for page in range(1, 19):
    time.sleep(1)
    url = 'https://bj.fang.lianjia.com/loupan/' + 'pg' + str(page) + '/'
    headers = {
        'User-Agent':
        'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36'
    }
    response = requests.get(url=url, headers=headers)
    selector = parsel.Selector(response.text)
    lis = selector.css('.resblock-list-wrapper li')
    dit = {}
    for li in lis:
        title = li.css('.resblock-name a::text').get().strip()
        dit['名称'] = title
        location1 = li.css('.resblock-location span::text').get().strip()
        dit['地理位置（字段1）'] = location1
        location2 = li.css('.resblock-location span::text').getall()[1].strip()
        dit['地理位置（字段2）'] = location2
        location2 = li.css('.resblock-location a::text').get().strip()
        dit['地理位置（字段3）'] = location2
        room = li.css('.resblock-room span::text').get()
        if room is not None:
            room = room.strip()
        dit['房型'] = room
        area = li.css('.resblock-area span::text').get()
        '''如果面积为空，那么不写入该行'''
        if area is None:
            continue
        area = area.lstrip('建面 ').rstrip('㎡').split('-')[0]
        dit['面积（㎡）'] = area
        unitPrice = li.css('.main-price span::text').get()
        total = li.css('.second::text').get()
        '''如果total为空，说明没有均价'''
        if total is None:
            total = unitPrice.split('-')[0]
            unitPrice = str(round((eval(total) / eval(area)) * 10000))
            total = str(format(eval(total), '.4f'))
        else:
            '''如果total不为空，就用单价来算总价'''
            total = str(format((eval(unitPrice) * eval(area)) / 10000, '.4f'))
        dit['均价（元/平米）'] = unitPrice
        dit['总价（万元/套）'] = total
        csv_writer1.writerow(dit)
