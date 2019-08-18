




#
# 对一个列表迭代化之后，再有序的进行遍历
# for i in iter(list):
#     print(i)
import time

from lxml import etree
import requests
import re
from lxml import etree
import datetime
import pymysql
from multiprocessing import Pool
#特殊异常要先引入
from requests.exceptions import RequestException
#请求页面 #反爬虫升级 ，js渲染，selenium
from selenium import webdriver
from lxml import etree
import datetime

def call_page(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.text
        return None
    except RequestException:
        return None




# 将怕取到的代码设置为全局变量



#解析页面  思考把代码做一个接口或队列，公用
# 所有 coding, location,name,net_assets

# 用python操作mysql,进行遍历查询，然后返回一个结果。这里需要专门编写一个函数，作为生成器！
# 使用pymysql,还是使用sqlalchempy 可以作深入的思考！

# 思考遍历mysql数据库而不进行查询(个股解析应该已经没有问题了)


# 还是考虑使用正则算了 正则的编写要按照元素的顺序来做
def parse_stock_note(html):
    patt = re.compile('<dt>(.*?)</dt>'+'.*?<a href=".*?">(.*?)</a></dd>'+
                      '.*?<th class="symbol"><h1>(.*?)</h1></th>'+'.*?<td class="stoksPrice">(.*?)</td>'+'.*?<div class="ymuiHeader ymuiHeaderBGDark"><h2 class="ymuiTitle">参考指標</h2></div>'
                      +'.*?<strong>(.*?)</strong>'+'.*?<strong>(.*?)</strong>'+'.*?<strong>(.*?)</strong>'
                      +'.*?<dt class="title">最低購入代金'+'.*?<strong>(.*?)</strong>',re.S)
    items = re.findall(patt,html)
    big_list = []   # 存储到mysql中必须要是在列表中的元组！
    for item in items:
        big_list.append(item)

    return big_list
    # selector = etree.HTML(html)

    # code = selector.xpath('//*[@id="stockinf"]/div[1]/div[2]/dl/dt/text()')
    # name = selector.xpath('//*[@id="stockinf"]/div[1]/div[2]/table/tbody/tr/th/h1/text()')
    # industry = selector.xpath('//*[@id="stockinf"]/div[1]/div[2]/dl/dd[1]/a/text()')
    # market_value = selector.xpath('//*[@id="rfindex"]/div[2]/div[1]/dl/dd/strong/text()')
    # share_nums = selector.xpath('//*[@id="rfindex"]/div[2]/div[2]/dl/dd/strong/text()')
    # returns_ratio = selector.xpath('//*[@id="rfindex"]/div[2]/div[3]/dl/dd/strong/text()')
    # min_callMoney = selector.xpath('//*[@id="rfindex"]/div[2]/div[9]/dl/dd/strong/text()')
    # # 算是财务个股数据，暂时不做
    # for i1,i2,i3,i4,i5,i6,i7 in zip(code,name,industry,market_value,share_nums,returns_ratio,min_callMoney):
    #     print (i1,i2,i3,i4,i5,i6,i7)


# 可以思考把数据库的所有操作放在一个类里面，数据库的连接，查询，返回值，然后在插入
# 就是对于具体类中的方法如何进行调用  也要尝试取思考如何去使用类！如何取编写类！
# 其实在一个脚本里面，没有必要写的过于复杂！ 借鉴专门做一个配置的模块，增强代码的复用性！
# 后端工程师，编写API接口，很重要的还是跟数据库的交互，所以Pymysql已经在踩坑了，Pymongo也要开始踩坑！
#传回去的数据结构只需要是json即可！ 查询和使用是异步请求的！所以最好遍历查询，然后请求，之后再来下一个

# 查询的方法
def Python_sel_Mysql():
    # 使用cursor()方法获取操作游标
    connection = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='123456', db='JS',
                                 charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)
    cur = connection.cursor()
    #sql 语句
    for i in range(3591,3700):
        sql = 'select coding from js_infos where id = %s ' % i
        # #执行sql语句
        cur.execute(sql)
        # #获取所有记录列表
        data = cur.fetchone()
        Num = data['coding']
        url = 'https://stocks.finance.yahoo.co.jp/stocks/detail/?code=' + str(Num) +'.t'
        yield url





def insertDB(content):
    connection = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='123456', db='JS',
                                 charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)

    cursor = connection.cursor()
    try:
        cursor.executemany('insert into js_infos_finanData (coding,industry,title,last_price,market_value,share_nums,returns_ratio,min_callshares) values (%s,%s,%s,%s,%s,%s,%s,%s)', content)
        connection.commit()
        connection.close()
        print('向MySQL中添加数据成功！')
    except TypeError :
        pass

# 存在重复爬取的情况，还有就是会变动的数据还是要等到交易闭市之后再爬取，数据才不会变动！

# 3589条有遗漏，不知道是不是因为用了进程池的原因！

# 使用yield 之后可以让一个函数变成生成器 ，这是一个可以存储数据的数据容器，直接进行遍历即可！因为内含__next__方法
# 对于生成器的时候必须加上括号！
if __name__ == '__main__':
    for url_str in Python_sel_Mysql():

        html = call_page(url_str)
        content = parse_stock_note(html)
        insertDB(content)
        print(datetime.datetime.now())


# url = 'https://stocks.finance.yahoo.co.jp/stocks/detail/?code=6178.t'
# html = call_page(url)
# content = parse_stock_note(html)
# insertDB(content)



# # name是mysql的关键字！
# create table js_infos_finanData(
# id int not null primary key auto_increment,
# coding varchar(11),
# industry varchar(8),
# title varchar(60),
# last_price varchar(20),
# market_value varchar(20),
# share_nums varchar(30),
# returns_ratio varchar(6),
# min_callshares varchar(11)
# ) engine=InnoDB default charset=utf8;



# drop table js_infos_finanData;

# coding,industry,name,last_price,market_value,share_nums,returns_ratio,min_callshares

# select id,coding,industry,title,market_value,returns_ratio from js_infos_finanData;