import requests
import csv
import parsel
import time
from requests.adapters import HTTPAdapter


# 构造随机函数
def get_ua():
    import random
    user_agents = [
        'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36 OPR/26.0.1656.60',
        'Opera/8.0 (Windows NT 5.1; U; en)',
        'Mozilla/5.0 (Windows NT 5.1; U; en; rv:1.8.1) Gecko/20061208 Firefox/2.0.0 Opera 9.50',
        'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; en) Opera 9.50',
        'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:34.0) Gecko/20100101 Firefox/34.0',
        'Mozilla/5.0 (X11; U; Linux x86_64; zh-CN; rv:1.9.2.10) Gecko/20100922 Ubuntu/10.10 (maverick) Firefox/3.6.10',
        'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/534.57.2 (KHTML, like Gecko) Version/5.1.7 Safari/534.57.2 ',
        'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.71 Safari/537.36',
        'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
        'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/534.16 (KHTML, like Gecko) Chrome/10.0.648.133 Safari/534.16',
        'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/30.0.1599.101 Safari/537.36',
        'Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko',
        'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.11 TaoBrowser/2.0 Safari/536.11',
        'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.71 Safari/537.1 LBBROWSER',
        'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; QQDownload 732; .NET4.0C; .NET4.0E)',
        'Mozilla/5.0 (Windows NT 5.1) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.84 Safari/535.11 SE 2.X MetaSr 1.0',
        'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; SV1; QQDownload 732; .NET4.0C; .NET4.0E; SE 2.X MetaSr 1.0) ',
    ]
    user_agent = random.choice(user_agents)  # 随机抽取对象
    return user_agent


f1 = open('Yzbeijing.csv', mode='a+', encoding='utf-8', newline='')
f2 = open('Yzshanghai.csv', mode='a+', encoding='utf-8', newline='')
f3 = open('Yzguangzhou.csv', mode='a+', encoding='utf-8', newline='')
f4 = open('Yzshenzhen.csv', mode='a+', encoding='utf-8', newline='')
f5 = open('Yzchangde.csv', mode='a+', encoding='utf-8', newline='')

csv_writer1 = csv.DictWriter(
    f1, fieldnames=['名称', '区', '板块', '具体地址', '面积（㎡）', '朝向', '房型', '租价（元/月）'])
csv_writer2 = csv.DictWriter(
    f2, fieldnames=['名称', '区', '板块', '具体地址', '面积（㎡）', '朝向', '房型', '租价（元/月）'])
csv_writer3 = csv.DictWriter(
    f3, fieldnames=['名称', '区', '板块', '具体地址', '面积（㎡）', '朝向', '房型', '租价（元/月）'])
csv_writer4 = csv.DictWriter(
    f4, fieldnames=['名称', '区', '板块', '具体地址', '面积（㎡）', '朝向', '房型', '租价（元/月）'])
csv_writer5 = csv.DictWriter(
    f5, fieldnames=['名称', '区', '板块', '具体地址', '面积（㎡）', '朝向', '房型', '租价（元/月）'])

csv_writer1.writeheader()
csv_writer2.writeheader()
csv_writer3.writeheader()
csv_writer4.writeheader()
csv_writer5.writeheader()

csv_writer = [csv_writer1, csv_writer2, csv_writer3, csv_writer4, csv_writer5]
city = ['bj', 'sh', 'gz', 'sz', 'changde']

s = requests.session()
s.mount('http://', HTTPAdapter(max_retries=3))
s.mount('https://', HTTPAdapter(max_retries=3))

for i in range(0, 5):  # 城市遍历
    for page in range(1, 101):
        if page % 10 == 0:
            time.sleep(1)
        url = 'https://' + city[i] + '.lianjia.com/zufang/' + 'orec1pg' + str(
            page) + '/'
        headers = {'User-Agent': get_ua()}
        response = s.get(url=url, headers=headers, timeout=10)
        selector = parsel.Selector(response.text)
        lis = selector.css('.content__list .content__list--item')
        print(url)
        if len(lis) == 8:  # 如果只有八套则一定均为推荐房源
            break
        cnt = 0
        for li in lis:
            cnt = cnt + 1
            dit = {}
            title = li.css('.twoline::text').get().strip('"').strip()
            if title == '':
                title = li.css('.content__list--item--title a::text').get(
                ).strip('"').strip()
            dit['名称'] = title
            if len(li.css('.content__list--item--des a::text').getall()) > 2:
                location1 = li.css('.content__list--item--des a::text').get()
                dit['区'] = location1
                location2 = li.css(
                    '.content__list--item--des a::text').getall()[1]
                dit['板块'] = location2
                location3 = li.css(
                    '.content__list--item--des a::text').getall()[2]
                dit['具体地址'] = location3
            if len(li.css('.content__list--item--des::text').getall()) == 8:
                area = li.css('.content__list--item--des::text').getall(
                )[4].strip('"').strip()
                to = li.css('.content__list--item--des::text').getall(
                )[5].strip('"').strip()
                room = li.css('.content__list--item--des::text').getall(
                )[6].strip('"').strip()
            elif len(li.css('.content__list--item--des::text').getall()) == 5:
                area = li.css('.content__list--item--des::text').getall(
                )[2].strip('"').strip()
                to = li.css('.content__list--item--des::text').getall(
                )[3].strip('"').strip()
                room = li.css('.content__list--item--des::text').getall(
                )[4].strip('"').strip()
            elif len(li.css('.content__list--item--des::text').getall()) == 3:
                area = li.css('.content__list--item--des::text').getall(
                )[0].strip('"').strip()
                to = li.css('.content__list--item--des::text').getall(
                )[1].strip('"').strip()
                room = li.css('.content__list--item--des::text').getall(
                )[2].strip('"').strip()
            elif len(li.css('.content__list--item--des::text').getall()) == 9:
                area = li.css('.content__list--item--des::text').getall(
                )[5].strip('"').strip()
                to = li.css('.content__list--item--des::text').getall(
                )[6].strip('"').strip()
                room = li.css('.content__list--item--des::text').getall(
                )[7].strip('"').strip()
            else:
                print(len(li.css('.content__list--item--des::text').getall()))
                print(title)
            if '㎡' in area:
                dit['面积（㎡）'] = area.rstrip('㎡')
            if '租' not in to:
                dit['朝向'] = to
            dit['房型'] = room
            price = li.css('.content__list--item-price em::text').get()
            dit['租价（元/月）'] = price
            csv_writer[i].writerow(dit)
            if (len(lis) < 30 and len(lis) - cnt <=
                    8):  # 如果本页总租房数小于 30 且当前只剩八套，则该八套一定是推荐房源 ，进行break
                break
        if len(lis) < 30:  # 如果已经没有信息了就跳过本次筛选
            break