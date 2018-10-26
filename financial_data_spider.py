# -*- coding:utf-8 -*-
import datetime
import re
import time

import pymysql
import requests
from lxml import etree

from selenium import webdriver

driver = webdriver.Chrome()
from requests.exceptions import RequestException


def get_first_page(url):

    driver.get(url)
    time.sleep(3)

    html = driver.page_source
    return html





def parse_stock_note(html):


    selector = etree.HTML(html)

    code = selector.xpath('//*[@id="kobetsu_data"]/table[1]/tbody/tr[1]/td/table/tbody/tr/td[1]/text()')
    return code
    # patt1 = re.compile('<td width="36">(.*?)</td>',re.S)
    # items1 = re.findall(patt1,html)
    # patt2 = re.compile('&nbsp;</span> (.*?)</td>',re.S)
    # item2 = re.findall(patt2,html)
    # # big_list = []   # 存储到mysql中必须要是在列表中的元组！
    # # for item in items:
    # #     big_list.append(item)
    # return item2






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
        num = data['coding']
        url = 'https://kabutan.jp/stock/finance?code=' + str(num) +'&mode=k#zaimu_zisseki'
        yield url



def insertDB(content):
    connection = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='123456', db='JS',
                                 charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)

    cursor = connection.cursor()
    try:
        cursor.executemany('insert into js_FinData (coding,DAT,profits) values (%s,%s)', content)
        connection.commit()
        connection.close()
        print('向MySQL中添加数据成功！')
    except TypeError :
        pass


if __name__ == '__main__':
    # for url_str in Python_sel_Mysql():
    url_str = 'https://kabutan.jp/stock/finance?code=3563&mode=k#zaimu_zisseki'
    html = get_first_page(url_str)
    content = parse_stock_note(html)
    print(content)
    # print(html)


    # insertDB(content)
    # print(datetime.datetime.now())


# create table js_FinData(
# id int not null primary key auto_increment,
# coding varchar(8),
# DAT varchar(11),
# profits varchar(20)
# ) engine=InnoDB default charset=utf8;