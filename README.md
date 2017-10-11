# ShenZhenRentSpider
python3.5 + scrapy1.4 爬取房天下深圳租房信息
<br>
问题点及进展：
<br>
1、爬取两个页面就断开 (已修复，能一直往下爬取)
<br>
2、之前爬取页面第二个页面之后会爬取不到数据，是因为列表的XPATH首页跟子页面有所不同（已修复） 2017-10-09
<br>
3、同2问题点导致后面页面爬取数据为None（已修复） 2017-10-10
<br>
3、问题点为爬取网页存储的数据量与核算的数据量不全（待修复）
<br>
输入下列命令执行爬虫，并将爬取数据存入test.csv
<br>
scrapy crawl ftx -o test.csv
<br>
输入下列命令执行爬虫则直接爬取数据并存储在FangTianXia.json文件内
<br>
scrapy crawl ftx
<br>

功能优化日历
<br>
1、20170922 增加json数据存储
<br>
2、20171009 修复爬取页面下一页之后会爬取不到数据的问题
<br>
3、20171010 修复爬取数据为None问题，Setting中增加自动限速(AutoThrottle)扩展
<br>
4、20171011 增加MySql数据库存储
<br>
<br>
-------------<br>
QQ：357270546<br>
-------------<br>
<br>

