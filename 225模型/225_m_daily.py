


import datetime
import time

import pymysql
import requests
from lxml import etree
import json
from queue import Queue
import threading
from requests.exceptions import RequestException




from retrying import retry

def retry_if_io_error(exception):
    return isinstance(exception, ZeroDivisionError)






'''
1. 创建 URL队列, 响应队列, 数据队列 在init方法中
2. 在生成URL列表中方法中,把URL添加URL队列中
3. 在请求页面的方法中,从URL队列中取出URL执行,把获取到的响应数据添加响应队列中
4. 在处理数据的方法中,从响应队列中取出页面内容进行解析, 把解析结果存储数据队列中
5. 在保存数据的方法中, 从数据队列中取出数据,进行保存
6. 开启几个线程来执行上面的方法
'''

def run_forever(func):
    def wrapper(obj):
        while True:
            func(obj)
    return wrapper


def RemoveDot(item):
    f_l = []
    for it in item:

        f_str = "".join(it.split(","))
        ff_str = f_str +"00"
        f_l.append(ff_str)

    return f_l

def remove_douhao(num):
    num1 = "".join(num.split(","))
    f_num = str(num1)
    return f_num
def remove_block(items):
    new_items = []
    for it in items:
        f = "".join(it.split())
        new_items.append(f)
    return new_items

def call_page(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.text
        return None
    except RequestException:
        return None

class JSPool_M(object):

    def __init__(self,url):
        self.url = url

    def page_request(self):
        ''' 发送请求获取数据 '''
        headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36'
        }

        response = requests.get(self.url,headers=headers)
        if response.status_code == 200:
            html = response.text
            return html
        else:
            pass

    def page_parse_(self):
        '''根据页面内容使用lxml解析数据, 获取段子列表'''


        html  = self.page_request()
        element = etree.HTML(html)

        now_price = element.xpath(
            '//*[@id="layout"]/div[2]/div[3]/div[2]/div/div[1]/div/div/div[1]/div[2]/div/div[2]/div/text()')
        f_price = RemoveDot(remove_block(now_price))
        big_list.append(f_price[0])
        return big_list




def insertDB(content):
    connection = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='123456', db='JS_Mons',
                                 charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)

    cursor = connection.cursor()

    try:
        # 用一个列表解析
        f_jsp = ["J" + str(cod) for cod in jl_db]
        sp_func = lambda x: ",".join(x)
        f_lcode = sp_func(f_jsp)

        f_ls = "%s," * len(jl_db)# 这里错了
        cursor.executemany('insert into sp_LJ_225 ({0}) values ({1})'.format(f_lcode, f_ls[:-1]), content)
        connection.commit()
        connection.commit()
        connection.close()
        print('向MySQL中添加数据成功！')
    except TypeError:
        pass








if __name__ == '__main__':
    jl_db = [1925,2801,4568,4578,6361,6841,7004,7912,8331,8804,8830,9433,9983,"_index225"]
    jl_web = [1925,2801,4568,4578,6361,6841,7004,7912,8331,8804,8830,9433,9983,100000018]

    big_list = []


    for it in jl_web:
        url = 'https://minkabu.jp/stock/{0}'.format(it)
        print(url)
        jsp = JSPool_M(url)# 这里把请求和解析都进行了处理
        jsp.page_parse_()
    ff_l = []
    f_tup = tuple(big_list)
    ff_l.append((f_tup))
    print(ff_l)
    insertDB(ff_l)
























 # create table sp_LJ_225(id int not null primary key auto_increment, J1925 float,J2801 float,J4568 float,J4578 float,J6361 float,J6841 float,J7004 float,J7912 float,J8331 float,J8804 float,J8830 float,J9433 float,J9983 float,J_index225 float, LastTime timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP ) engine=InnoDB  charset=utf8;
