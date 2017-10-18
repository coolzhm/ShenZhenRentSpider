# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import codecs
import json
import pymysql


class ShenzhenrentspiderPipeline(object):
    def __init__(self):
        self.file = codecs.open('FangTianXia.json', 'w+', encoding='utf-8')

    def process_item(self, item, spider):
        # print ('[========= {0} =========]'.format(item['url']))
        line = json.dumps(dict(item), ensure_ascii=False) + "\n"
        self.file.write(line)
        return item

    def spider_closed(self, spider):
        self.file.close()


# 将爬取数据存入MYSQL
class SaveDataToMySQLPipeline(object):
    config = {
        'host': 'localhost',
        'port': 3306,
        'user': 'root',
        'password': 'a8616645',
        'db': 'test',
        'charset': 'utf8mb4'
    }

    def __init__(self):
        print(">>>>>>>>>>>>>>>> 准备写入MySQL数据库 <<<<<<<<<<<<<<<<<")

    def process_item(self, item, spider):
        # 创建连接
        connection = pymysql.connect(**self.config)

        try:
            with connection.cursor() as cursor:
                sql = "INSERT INTO fangtianxia (id,title,area,place,village,location,price,unit,rentstyle,renttype,size,info,url) " \
                      "VALUES (nextval('fangtianxia'),'{0}','{1}','{2}','{3}','{4}','{5}','{6}','{7}','{8}','{9}','{10}','{11}')".format(
                    item['title'], item['area'], item['place'], item['village'], item['location'], item['price'],
                    item['unit'], item['rentstyle'], item['renttype'], item['size'], item['info'], item['url'])
                cursor.execute(sql)
                connection.commit()
        finally:
            connection.close()

    def spider_closed(self, spider):
        print(">>>>>>>>>>>>>>>> 写入MySQL数据库完成 <<<<<<<<<<<<<<<<<")
