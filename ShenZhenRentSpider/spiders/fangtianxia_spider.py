# -*- coding: utf-8 -*-

from scrapy.spider import Spider
import scrapy
from ShenZhenRentSpider.items import HouseInfoItem


class FangTianXiaSpider(Spider):
    name = 'ftx'
    # 减慢爬取速度 为1s
    # download_delay = 1
    start_urls = [
        'http://zu.sz.fang.com'
    ]
    aa = 1
    allowed_domains = ['fang.com', 'zu.sz.fang.com', 'zu.sz.fang.com/house/']

    # 遍历爬取
    def parse(self, response):
        baseurl = 'http://zu.sz.fang.com'
        # 爬取页面信息
        list = response.xpath('//*[@class="houseList"]/dl')
        print('------ 准备爬取第【{1}】网页 "{0}" 信息 ------'.format(response.url, self.aa))
        print('========当前页面共有 {0} 个房源========='.format(len(list)))
        for i in range(1, len(list) + 1):
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

            yield scrapy.Request(detail_url, callback=self.parse_rent_info, meta={'item': item})

        # 遍历页码的标签，查看是否存在 下一页
        pagelist = response.xpath('//*[@id="rentid_D10_01"]/a')
        for j in range(1, len(pagelist) + 1):
            value = response.xpath('//*[@id="rentid_D10_01"]/a[{0}]/text()'.format(j)).extract_first()
            next_url = response.xpath('//*[@id="rentid_D10_01"]/a[%s]/@href' % j).extract_first()
            result = u'下一页' in str(value)
            if (result):
                yield scrapy.Request("http://zu.sz.fang.com{0}".format(next_url), callback=self.parse)

        print('----------------------- 爬取第【{0}】页面结束 --------------------------'.format(self.aa))
        # 计数
        self.aa = self.aa + 1

    # 进入子页面获取内容
    def parse_rent_info(self, response):
        item = response.meta['item']
        item['renttype'] = response.xpath('/html/body/div[6]/div[3]/div[2]/ul[1]/li[1]/text()').extract_first()
        item['location'] = response.xpath('/html/body/div[6]/div[3]/div[2]/ul[1]/li[4]/@title').extract_first()
        yield item
