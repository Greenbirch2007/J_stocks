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
    profits= selector.xpath('//*[@id="right_col"]/table/tbody/tr[1]/td/table/tbody/tr[7]/td/text()')


    big_tuple = (code[0],profits[1][:-3],profits[2][:-3],profits[3][:-3])
    big_list.append(big_tuple)
    return big_list








def Python_sel_Mysql():
    # 使用cursor()方法获取操作游标
    connection = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='123456', db='JS',
                                 charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)
    cur = connection.cursor()
    #sql 语句
    for i in range(1,3600):
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
        cursor.executemany('insert into js_FinData1 (coding,d2018,d2017,d2016) values (%s,%s,%s,%s)', content)
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




# create table js_FinData1(
# id int not null primary key auto_increment,
# coding varchar(50),
# d2018 varchar(20),
# d2017 varchar(20),
# d2016 varchar(20)
# ) engine=InnoDB default charset=utf8;