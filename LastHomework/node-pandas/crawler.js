const Crawler = require("crawler");
const CSV = require('fast-csv')
const File = require('fs')
const path = require('path')



const user_agents = [
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


const sleep = (delay) => new Promise((resolve) => setTimeout(resolve, delay))


const citys = ['bj', 'sh', 'gz', 'sz', 'changde']
const csvStream = CSV.format({ headers: ['名称', '区', '板块', '具体地址', '面积（㎡）', '朝向', '房型', '租价（元/月）']})

const cityMap = {bj : 'beijing', sh : 'shanghai', gz : 'guangzhou', sz : 'shenzhen', changde : 'changde'}



const manners = ['rt200600000001', 'rt200600000002']
const rentPrices = [
    'brp0erp1250', 'brp1251erp1500', 'brp1501erp1750', 'brp1751erp2000',
    'brp2001erp2500', 'brp2501erp3000', 'brp3001erp4000', 'brp4001erp5000',
    'brp5001erp6500', 'brp6501erp8000', 'brp8001erp20000', 'brp20001'
]
const roomTypes = ['l0', 'l1', 'l2', 'l3']
const areaTypes = ['ra0', 'ra1', 'ra2', 'ra3', 'ra4', 'ra5']

var csvStreams = new Map()


var testdes = []

var c = new Crawler({
    maxConnections : 10,
    rotateUA : true,
    userAgent : user_agents,

    // rateLimit : 500,

    // 在每个请求处理完毕后将调用此回调函数
    callback : function (error, res, done) {
        console.log(res.options.uri)
        if(error){
            console.log(error);
        }else{
            let city = res.options.city
            let $ = res.$;


            // 如果只有八套则一定均为推荐房源，跳过
            let listLen = $(".content__list--item--main").length
            if (listLen === 8) {
                done()
            }
            
            $(".content__list--item--main").each(function(i, elem) { // 遍历列表

                // 如果本页总租房数小于 30 且当前只剩八套，则该八套一定是推荐房源 ，不处理， 进行 break
                if (listLen < 30 && listLen - i <= 8) return 

                let info = []
                let title = $(this).children('.content__list--item--title').children('.twoline').text().trim() // 名字
                if (title.length === 0) {
                    title = $(this).children('.content__list--item--title').text().trim()
                }
                info.push(title) // 名字

                // console.log(title)
                let desLen1 = $(this).children('.content__list--item--des').children('a').length

                if (desLen1 > 2) {
                    $(this).children('.content__list--item--des').children('a').each(function(i, elem) {
                        switch(i) {
                            case 0: // 区
                            case 1: // 板块
                            case 2: // 具体地址
                                info.push($(this).text())
                                break
                            default:
                                console.log(i)
                        }
                    })
                } else {
                    for (i = 0; i < 3; i++) info.push('')
                }

                let desLen2 = $(this).children('.content__list--item--des').contents().length

                $(this).children('.content__list--item--des').contents().each(function(i, ele) {
                    switch(desLen2) {
                        case 15:
                            switch(i) {
                                case 8:
                                case 10:
                                case 12:
                                    info.push($(this).text().trim())
                                    //console.log($(this).text().trim())
                                    break
                                default:
                                    break
                            }
                            break
                        case 17:
                            switch(i) {
                                case 10:
                                case 12:
                                case 14:
                                    info.push($(this).text().trim())
                                    //console.log($(this).text().trim())
                                    break
                                default:
                                    break
                            }
                            break
                        case 9:
                            switch(i) {
                                case 4:
                                    info.push($(this).text().trim())
                                    info.push('')
                                    //console.log($(this).text().trim())
                                    break
                                case 8:
                                    info.push($(this).text().trim())
                                    //console.log($(this).text().trim())
                                    break
                                default:
                                    break
                            }
                            break
                            case 5:
                                switch(i) {
                                    case 0:
                                        info.push($(this).text().trim())
                                        //console.log($(this).text().trim())
                                        info.push('')
                                        break
                                    case 4:
                                        info.push($(this).text().trim())
                                        //console.log($(this).text().trim())
                                        break
                                    default:
                                        break
                                }
                                break
                            default:
                                console.log('desLen2' + toString(desLen2))
                    }
                })

                /* if (testdes.indexOf(desLen2) === -1) {
                    testdes.push(desLen2)
                    console.log("deslen2:" + desLen2)
                    $(this).children('.content__list--item--des').contents().each(function(i, ele) {
                        console.log("\t" + i + $(this).text().trim())
                    })  
                } */

                info.push($(this).children('.content__list--item-price').children('em').text().trim()) // 价格
                // console.log(info)
                csvStreams.get(city).write(info)
            })
        }
        done();
    }
});

function InitStream() {
    for (var key in cityMap) { // 创建csv文件
        let cityName = cityMap[key]
        let writeStream = File.createWriteStream(path.resolve(__dirname, cityName + '.csv'), {flags : 'w'})
        csvStreams.set(key, CSV.format({ headers: ['名称', '区', '板块', '具体地址', '面积（㎡）', '房型', '租价（元/月）']}))
        csvStreams.get(key).pipe(writeStream)
    }
}


async function main () {
    InitStream()
    // 条件遍历
    citys.forEach((city) => {
        manners.forEach((manner) => {
            roomTypes.forEach((roomType)=> {
                areaTypes.forEach((areaType)=> {
                    rentPrices.forEach(async (rentPrice)=>{
                        for (page = 1; page <= 100; page++) {
                            if (page % 10 === 0) {
                                await sleep(1000)
                            }
                            let url = 'https://' + city + '.lianjia.com/zufang/' + 'pg' + page + manner + roomType + areaType + rentPrice + '/'
                            c.queue({
                                uri : url,
                                city : city, 
                            })
                        }
                    })
                })
            })
        })
    })
    /* for (var city in citys) {
        for (var manner in manners) {
            for (var roomType in roomTypes) {
                for (var areaType in areaTypes) {
                    for (var rentPrice in rentPrices) {
                        
                    }
                }
            }
        }
    } */
}

/* InitStream()

for (i = 1; i < 2; i++) {
    c.queue({
        uri : 'https://bj.lianjia.com/zufang/pg' + toString(i),
        city : 'bj'
    })
} */

module.exports = {crawler : main}