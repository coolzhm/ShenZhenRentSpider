# -*- coding: utf-8 -*-
import random

from scrapy.spider import Spider
import scrapy
from ShenZhenRentSpider.items import HouseInfoItem


class FangTianXiaSpider(Spider):
    name = 'ftx'
    # 减慢爬取速度 为1s
    # download_delay = 0.25
    start_urls = [
        'http://zu.sz.fang.com'
    ]
    # 页面计数器
    page_count = 1
    # 数据量计数器
    data_count = 0
    allowed_domains = ['fang.com', 'zu.sz.fang.com', 'zu.sz.fang.com/house/']

    USER_AGENTS = [
        "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; AcooBrowser; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
        "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0; Acoo Browser; SLCC1; .NET CLR 2.0.50727; Media Center PC 5.0; .NET CLR 3.0.04506)",
        "Mozilla/4.0 (compatible; MSIE 7.0; AOL 9.5; AOLBuild 4337.35; Windows NT 5.1; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
        "Mozilla/5.0 (Windows; U; MSIE 9.0; Windows NT 9.0; en-US)",
        "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 2.0.50727; Media Center PC 6.0)",
        "Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 1.0.3705; .NET CLR 1.1.4322)",
        "Mozilla/4.0 (compatible; MSIE 7.0b; Windows NT 5.2; .NET CLR 1.1.4322; .NET CLR 2.0.50727; InfoPath.2; .NET CLR 3.0.04506.30)",
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN) AppleWebKit/523.15 (KHTML, like Gecko, Safari/419.3) Arora/0.3 (Change: 287 c9dfb30)",
        "Mozilla/5.0 (X11; U; Linux; en-US) AppleWebKit/527+ (KHTML, like Gecko, Safari/419.3) Arora/0.6",
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.2pre) Gecko/20070215 K-Ninja/2.1.1",
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN; rv:1.9) Gecko/20080705 Firefox/3.0 Kapiko/3.0",
        "Mozilla/5.0 (X11; Linux i686; U;) Gecko/20070322 Kazehakase/0.4.5",
        "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.8) Gecko Fedora/1.9.0.8-1.fc10 Kazehakase/0.5.6",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_3) AppleWebKit/535.20 (KHTML, like Gecko) Chrome/19.0.1036.7 Safari/535.20",
        "Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; fr) Presto/2.9.168 Version/11.52",
    ]

    # 遍历爬取
    def parse(self, response):
        baseurl = 'http://zu.sz.fang.com'
        # 爬取页面信息
        list = response.xpath('//*[@class="houseList"]/dl')
        print('------ 准备爬取第【{1}】网页 "{0}" 信息 ------'.format(response.url, self.page_count))
        print('========当前页面共有 {0} 个房源========='.format(len(list)))
        for i in range(1, len(list) + 1):
            self.data_count = self.data_count + 1
            print("--------- 现在爬取第{0}个数据！！！---------------".format(i))
            item = HouseInfoItem()
            item['title'] = response.xpath(
                '//*[@class="houseList"]/dl[{0}]/dd/p[1]/a/@title'.format(i)).extract_first()
            item['area'] = response.xpath(
                '//*[@class="houseList"]/dl[{0}]/dd/p[3]/a[1]/span/text()'.format(i)).extract_first()
            item['place'] = response.xpath(
                '//*[@class="houseList"]/dl[{0}]/dd/p[3]/a[2]/span/text()'.format(i)).extract_first()
            item['village'] = response.xpath(
                '//*[@class="houseList"]/dl[{0}]/dd/p[3]/a[3]/span/text()'.format(i)).extract_first()
            item['price'] = response.xpath(
                '//*[@class="houseList"]/dl[{0}]/dd/div[2]/p/span/text()'.format(i)).extract_first()
            item['unit'] = response.xpath(
                '//*[@class="houseList"]/dl[{0}]/dd/div[2]/p/text()'.format(i)).extract_first()
            item['rentstyle'] = response.xpath(
                '//*[@class="houseList"]/dl[{0}]/dd/p[2]/text()[1]'.format(i)).extract_first()
            # item['renttype'] = response.xpath('//*[@class="houseList"]/dl[{0}]/dd/p[2]/text()[1]'.format(i)).extract()
            item['size'] = response.xpath(
                '//*[@class="houseList"]/dl[{0}]/dd/p[2]/text()[3]'.format(i)).extract_first()
            item['info'] = response.xpath(
                '//*[@class="houseList"]/dl[{0}]/dd/p[2]/text()[2]'.format(i)).extract_first()
            item['url'] = response.xpath('//*[@class="houseList"]/dl[{0}]/dd/p[1]/a/@href'.format(i)).extract_first()

            detail_url = "http://zu.sz.fang.com{0}".format(
                response.xpath('//*[@class="houseList"]/dl[{0}]/dd/p[1]/a/@href'.format(i)).extract_first())

            headers = {
                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
                'Accept-Encoding': 'gzip, deflate',
                'Accept-Language': 'zh-CN,zh;q=0.8',
                'Cache-Control': 'max-age=0',
                'Connection': 'keep-alive',
                'User-Agent': random.choice(self.USER_AGENTS)
            }
            print('子页面当前User-Agent为：')
            print(headers['User-Agent'])

            yield scrapy.Request(detail_url, callback=self.parse_rent_info, meta={'item': item},headers=headers)

        # 遍历页码的标签，查看是否存在 下一页
        pagelist = response.xpath('//*[@id="rentid_D10_01"]/a')
        #此处自定义爬取页数
        if (self.page_count <= 100):
            for j in range(1, len(pagelist) + 1):
                value = response.xpath('//*[@id="rentid_D10_01"]/a[{0}]/text()'.format(j)).extract_first()
                next_url = response.xpath('//*[@id="rentid_D10_01"]/a[%s]/@href' % j).extract_first()
                result = u'下一页' in str(value)
                if (result):
                    headers = {
                        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
                        'Accept-Encoding': 'gzip, deflate',
                        'Accept-Language': 'zh-CN,zh;q=0.8',
                        'Cache-Control': 'max-age=0',
                        'Connection': 'keep-alive',
                        'User-Agent': random.choice(self.USER_AGENTS)
                    }
                    print('下一页面User-Agent为：')
                    print(headers['User-Agent'])

                    yield scrapy.Request("http://zu.sz.fang.com{0}".format(next_url), callback=self.parse, headers=headers)

            print('----------------------- 爬取第【{0}】页面结束 --------------------------'.format(self.page_count))
            print('----------------------- 总计爬取【{0}】数据量 --------------------------'.format(self.data_count))
            # 计数
            self.page_count = self.page_count + 1

    # 进入子页面获取内容
    def parse_rent_info(self, response):
        item = response.meta['item']
        item['renttype'] = response.xpath('/html/body/div[6]/div[3]/div[2]/ul[1]/li[1]/text()').extract_first()
        item['location'] = response.xpath('/html/body/div[6]/div[3]/div[2]/ul[1]/li[4]/@title').extract_first()
        yield item
