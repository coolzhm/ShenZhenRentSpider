# -*- coding: utf-8 -*-

import pymysql

#添加'charset': 'utf8mb4' 是为了防止中文变成乱码
config = {
    'host': 'localhost',
    'port': 3306,
    'user': 'root',
    'password': 'a8616645',
    'db': 'test',
    'charset': 'utf8mb4'
}

# 创建连接
connection = pymysql.connect(**config)

try:
    with connection.cursor() as cursor:
        sql = 'INSERT INTO testtable (testID,testName) VALUES ("3","地方")'
        cursor.execute(sql)
        connection.commit()
finally:
    connection.close()
