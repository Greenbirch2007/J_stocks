




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





def parse_stock_note(html):

    patt = re.compile('<th class="symbol"><h1>(.*?)</h1></th>' +
                      '<td colspan="3">(.*?)[<a href=".*?">周辺地図</a>]</td>',re.S)
    items = re.findall(patt,html)
    big_list = []   # 存储到mysql中必须要是在列表中的元组！
    for item in items:
        big_list.append(item)

    return big_list

# 查询的方法
def Python_sel_Mysql():
    # 使用cursor()方法获取操作游标
    connection = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='123456', db='JS',
                                 charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)
    cur = connection.cursor()
    #sql 语句
    for i in range(1,3700):
        sql = 'select coding from js_infos where id = %s ' % i
        # #执行sql语句
        cur.execute(sql)
        # #获取所有记录列表
        data = cur.fetchone()
        Num = data['coding']
        url = 'https://stocks.finance.yahoo.co.jp/stocks/profile/?code='+str(Num)+'.T'
        yield url





def insertDB(content):
    connection = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='123456', db='JS',
                                 charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)

    cursor = connection.cursor()
    try:
        cursor.executemany('insert into Company_location (CL) values (%s)', content)
        connection.commit()
        connection.close()
        print('向MySQL中添加数据成功！')
    except TypeError :
        pass


if __name__ == '__main__':
    for url_str in Python_sel_Mysql():

        html = call_page(url_str)
        content = parse_stock_note(html)
        print(content)
        # insertDB(content)
        # print(datetime.datetime.now())









# # name是mysql的关键字！
# create table Company_location(
# id int not null primary key auto_increment,
# CL text
# ) engine=InnoDB default charset=utf8;



# drop table Company_location;

# coding,industry,name,last_price,market_value,share_nums,returns_ratio,min_callshares

# select id,coding,industry,title,market_value,returns_ratio from js_infos_finanData;