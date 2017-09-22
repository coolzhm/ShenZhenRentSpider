# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from scrapy import Item,Field


class ShenzhenrentspiderItem(Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

class HouseInfoItem(Item):
    # 标题
    title = Field()
    #所属区域 如：宝安
    area = Field()
    #地名 如：沙井
    place = Field()
    #小区 如：大冲城市花园
    village = Field()
    # 详细地址、位置 如：南山蛇口望海路与金世纪路交汇处
    location = Field()
    # 租金
    price = Field()
    # 租金单位 如：元/月
    unit = Field()
    #租住形式 如：整租、合租
    rentstyle = Field()
    # 租金形式 如：押二付一
    renttype = Field()
    # 房屋大小 如：X平米
    size = Field()
    # 房屋信息 如：二室一厅一卫
    info = Field()
    # 网页地址
    url =Field()

