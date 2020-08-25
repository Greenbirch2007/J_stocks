# -*- coding:utf-8 -*-
import datetime
import re
import time

import pymysql

from lxml import etree
from selenium import webdriver

driver = webdriver.Chrome()


def get_first_page(url):

    driver.get(url)
    html = driver.page_source
    return html



# 可以尝试第二种解析方式，更加容易做计算
def parse_stock_note(html):
    big_list = []
    selector = etree.HTML(html)
    code = selector.xpath('//*[@id="pro_body"]/center/div[5]/h1/strong/text()')
    DAT_all = selector.xpath('//*[@id="right_col"]/table/tbody/tr[1]/td/table/tbody/tr[2]/td/text()')
    DAT_3 = DAT_all[1:4]
    profits_all = selector.xpath('//*[@id="right_col"]/table/tbody/tr[1]/td/table/tbody/tr[7]/td/text()')
    profits_3 = profits_all[1:4]
    code_3 = code * 3
    for i1,i2,i3 in zip(code_3, DAT_3, profits_3):
        big_tuple = (i1[-5:-1],i2,i3[:-3])
        big_list.append(big_tuple)
    return big_list







# 尝试在这个模块提取代码和板块，用代码去拼接个股链接，同时往大ｌist传入个股
def Python_sel_Mysql():
    # 使用cursor()方法获取操作游标
    connection = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='123456', db='JS',
                                 charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)
    cur = connection.cursor()
    #sql 语句
    for i in range(1,3651):
        sql = 'select coding from js_infos where id = %s ' % i
        # #执行sql语句
        cur.execute(sql)
        # #获取所有记录列表
        data = cur.fetchone()
        num = data['coding']
        url = 'https://profile.yahoo.co.jp/consolidate/' + str(num)
        yield url



def insertDB(content):
    connection = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='123456', db='JS',
                                 charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)

    cursor = connection.cursor()
    try:
        cursor.executemany('insert into js_FinData (coding,DAT,profits) values (%s,%s,%s)', content)
        connection.commit()
        connection.close()
        print('向MySQL中添加数据成功！')
    except TypeError :
        pass


if __name__ == '__main__':
    for url_str in Python_sel_Mysql():
        html = get_first_page(url_str)
        content = parse_stock_note(html)
        insertDB(content)
        print(datetime.datetime.now())


# create table js_FinData(
# id int not null primary key auto_increment,
# coding varchar(8),
# DAT varchar(11),
# profits varchar(20)
# ) engine=InnoDB default charset=utf8;
#
# create table js_FinData1(
# id int not null primary key auto_increment,
# coding varchar(8),
# d2018 varchar(20),
# d2017 varchar(20),
# d2016 varchar(20)
# ) engine=InnoDB default charset=utf8;