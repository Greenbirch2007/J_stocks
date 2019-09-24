

# 要点：价格，板块，市值！　就不断创建新的表，然后就用sql语言编写计算之后的收益率的情况

# 因为价格还是变化最频繁的，所以值采集价格动态数据，然后并表查询
import time

import requests
import re
import pymysql
from multiprocessing import Pool

from lxml import etree
from requests.exceptions import RequestException

#请求页面

def call_page(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.text
        return None
    except RequestException:
        return None

# 将怕取到的代码设置为全局变量

def remove_douhao(num):
    num1 = "".join(num.split(","))
    f_num = str(num1)
    return f_num

#解析页面  思考把代码做一个接口或队列，公用
# 所有 coding, location,name,net_assets
def parse_all_pages_one(html):  # 不要一次把正则弄伤了
    big_list = []
    selector = etree.HTML(html)

    code = selector.xpath('//*[@id="contents-body-bottom"]/div[2]/div[4]/table/tbody/tr/td[2]/a/text()')
    name = selector.xpath('//*[@id="contents-body-bottom"]/div[2]/div[4]/table/tbody/tr/td[4]/text()')
    now_price = selector.xpath('//*[@id="contents-body-bottom"]/div[2]/div[4]/table/tbody/tr/td[6]/text()')
    f_price =[]
    for item in now_price:
        fp = remove_douhao(item)
        f_price.append(fp)
    for i1,i2,i3 in zip(code,name,f_price):
        big_list.append((i1,i2,i3))

    return big_list








def insertDB(content):
    connection = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='123456', db='JS',
                                 charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)
    cur = connection.cursor()
    cur.executemany('insert into js_p0924 (code,name,f_price) values (%s,%s,%s)', content)
    connection.commit()
    connection.close()
    print('向MySQL中添加数据成功！')



if __name__ == '__main__':

    for offset in range(1,75):
        url = 'https://info.finance.yahoo.co.jp/ranking/?kd=53&tm=d&vl=a&mk=1&p=' + str(offset)
        html = call_page(url)
        time.sleep(1)

        content =parse_all_pages_one(html)
        insertDB(content)
        print(offset)

# #
# create table js_p0929(
# id int not null primary key auto_increment,
# code varchar(11),
# name varchar(100),
# f_price varchar(20),
# LastTime timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
# ) engine=InnoDB default charset=utf8;

# drop  table js_p0929;

#　并表查询　
# select js_p0929.name, js_p0929.f_price as a_p ,(js_p0929.f_price -js_p0924.f_price)/js_p0924.f_price pr,
# js_infos_finanData.coding, js_infos_finanData.industry,js_infos_finanData.market_value
# from  js_p0924,js_p0929,js_infos_finanData  where js_p0924.code=js_p0929.code  and js_p0929.code =js_infos_finanData.coding;