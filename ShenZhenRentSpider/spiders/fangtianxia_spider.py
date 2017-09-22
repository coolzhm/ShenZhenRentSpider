# -*- coding: utf-8 -*-

from scrapy.spider import Spider
import scrapy
import re
from ShenZhenRentSpider.items import HouseInfoItem


class FangTianXiaSpider(Spider):
    name = 'ftx'
    allowed_domains = ['fang.com', 'http://zu.sz.fang.com']
    start_urls = [
        'http://zu.sz.fang.com/'
    ]

    # 遍历爬取
    def parse(self, response):
        baseurl = 'http://zu.sz.fang.com'
        # 爬取页面信息
        list = response.xpath('//*[@id="listBox"]/div[3]/dl')
        for i in range(1, len(list) + 1):
            print("---------现在爬取第{0}个数据！！！---------------".format(i))
            item = HouseInfoItem()
            item['title'] = response.xpath(
                '//*[@id="listBox"]/div[3]/dl[{0}]/dd/p[1]/a/@title'.format(i)).extract_first()
            item['area'] = response.xpath(
                '//*[@id="listBox"]/div[3]/dl[{0}]/dd/p[3]/a[1]/span/text()'.format(i)).extract_first()
            item['location'] = response.xpath(
                '//*[@id="listBox"]/div[3]/dl[{0}]/dd/p[3]/a[2]/span/text()'.format(i)).extract_first()
            item['price'] = response.xpath(
                '//*[@id="listBox"]/div[3]/dl[{0}]/dd/div[2]/p/span/text()'.format(i)).extract_first()
            item['unit'] = response.xpath(
                '//*[@id="listBox"]/div[3]/dl[{0}]/dd/div[2]/p/text()'.format(i)).extract_first()
            item['rentstyle'] = response.xpath(
                '//*[@id="listBox"]/div[3]/dl[{0}]/dd/p[2]/text()[1]'.format(i)).extract_first()
            # item['renttype'] = response.xpath('//*[@id="listBox"]/div[3]/dl[{0}]/dd/p[2]/text()[1]'.format(i)).extract()
            item['size'] = response.xpath(
                '//*[@id="listBox"]/div[3]/dl[{0}]/dd/p[2]/text()[3]'.format(i)).extract_first()
            item['info'] = response.xpath(
                '//*[@id="listBox"]/div[3]/dl[{0}]/dd/p[2]/text()[2]'.format(i)).extract_first()
            item['url'] = response.xpath('//*[@id="listBox"]/div[3]/dl[{0}]/dd/p[1]/a/@href'.format(i)).extract_first()
            yield item

        # 遍历页码的标签，查看是否存在 下一页
        pagelist = response.xpath('//*[@id="rentid_D10_01"]/a')
        for j in range(1, len(pagelist) + 1):
            value = response.xpath('//*[@id="rentid_D10_01"]/a[{0}]/text()'.format(j)).extract_first()
            next_url = response.xpath('//*[@id="rentid_D10_01"]/a/@href').extract_first()
            # re.match('')
            result = u'下一页' in str(value)
            if (result):
                yield scrapy.Request("http://zu.sz.fang.com{0}".format(next_url),callback=self.parse)
            # print('************* 内容：{0} 结果：{1} *****************'.format(value, result))
        print('----------------------- 爬取结束 ----------------------------')

    # 爬取页面内容
    def parse_rent_info(self, response):
        baseurl = 'http://zu.sz.fang.com'
