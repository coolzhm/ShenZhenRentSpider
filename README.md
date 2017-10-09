# ShenZhenRentSpider
python3.5 + scrapy1.4 爬取房天下深圳租房信息
问题点及进展：
1、爬取两个页面就断开 (已修复，能一直往下爬取)
2、之前爬取页面第二个页面之后会爬取不到数据，是因为列表的XPATH首页跟子页面有所不同（已修复） 2017-10-09

输入下列命令执行爬虫，并将爬取数据存入test.csv
scrapy crawl ftx -o test.csv

功能优化日历
1、20170922 增加json数据存储


