


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
    jl_db = [4151,4502,4503,4506,4507,4519,4523,4568,4578,3105,6479,6501,6503,6504,6506,6645,6674,6701,6702,6703,6724,6752,6758,6762,6770,6841,6857,6902,6952,6954,6971,6976,7735,7751,7752,8035,7201,7202,7203,7205,7211,7261,7267,7269,7270,7272,4543,4902,7731,7733,7762,9412,9432,9433,9437,9613,9984,7186,8303,8304,8306,8308,8309,8316,8331,8354,8355,8411,8253,8697,8601,8604,8628,8630,8725,8750,8766,8795,1332,1333,2002,2269,2282,2501,2502,2503,2531,2801,2802,2871,2914,3086,3099,3382,8028,8233,8252,8267,9983,2413,2432,4324,4689,4704,4751,4755,6098,6178,9602,9735,9766,1605,3101,3103,3401,3402,3861,3863,3405,3407,4004,4005,4021,4042,4043,4061,4063,4183,4188,4208,4272,4452,4631,4901,4911,6988,5019,5020,5101,5108,5201,5202,5214,5232,5233,5301,5332,5333,5401,5406,5411,5541,3436,5703,5706,5707,5711,5713,5714,5801,5802,5803,5901,2768,8001,8002,8015,8031,8053,8058,1721,1801,1802,1803,1808,1812,1925,1928,1963,5631,6103,6113,6301,6302,6305,6326,6361,6367,6471,6472,6473,7004,7011,7013,7003,7012,7832,7911,7912,7951,3289,8801,8802,8804,8830,9001,9005,9007,9008,9009,9020,9021,9022,9062,9064,9101,9104,9107,9202,9301,9501,9502,9503,9531,9532]
    jl_web = jl_db

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
























# create table sp_LJ_225(id int not null primary key auto_increment, J4151 FLOAT,J4502 FLOAT,J4503 FLOAT,J4506 FLOAT,J4507 FLOAT,J4519 FLOAT,J4523 FLOAT,J4568 FLOAT,J4578 FLOAT,J3105 FLOAT,J6479 FLOAT,J6501 FLOAT,J6503 FLOAT,J6504 FLOAT,J6506 FLOAT,J6645 FLOAT,J6674 FLOAT,J6701 FLOAT,J6702 FLOAT,J6703 FLOAT,J6724 FLOAT,J6752 FLOAT,J6758 FLOAT,J6762 FLOAT,J6770 FLOAT,J6841 FLOAT,J6857 FLOAT,J6902 FLOAT,J6952 FLOAT,J6954 FLOAT,J6971 FLOAT,J6976 FLOAT,J7735 FLOAT,J7751 FLOAT,J7752 FLOAT,J8035 FLOAT,J7201 FLOAT,J7202 FLOAT,J7203 FLOAT,J7205 FLOAT,J7211 FLOAT,J7261 FLOAT,J7267 FLOAT,J7269 FLOAT,J7270 FLOAT,J7272 FLOAT,J4543 FLOAT,J4902 FLOAT,J7731 FLOAT,J7733 FLOAT,J7762 FLOAT,J9412 FLOAT,J9432 FLOAT,J9433 FLOAT,J9437 FLOAT,J9613 FLOAT,J9984 FLOAT,J7186 FLOAT,J8303 FLOAT,J8304 FLOAT,J8306 FLOAT,J8308 FLOAT,J8309 FLOAT,J8316 FLOAT,J8331 FLOAT,J8354 FLOAT,J8355 FLOAT,J8411 FLOAT,J8253 FLOAT,J8697 FLOAT,J8601 FLOAT,J8604 FLOAT,J8628 FLOAT,J8630 FLOAT,J8725 FLOAT,J8750 FLOAT,J8766 FLOAT,J8795 FLOAT,J1332 FLOAT,J1333 FLOAT,J2002 FLOAT,J2269 FLOAT,J2282 FLOAT,J2501 FLOAT,J2502 FLOAT,J2503 FLOAT,J2531 FLOAT,J2801 FLOAT,J2802 FLOAT,J2871 FLOAT,J2914 FLOAT,J3086 FLOAT,J3099 FLOAT,J3382 FLOAT,J8028 FLOAT,J8233 FLOAT,J8252 FLOAT,J8267 FLOAT,J9983 FLOAT,J2413 FLOAT,J2432 FLOAT,J4324 FLOAT,J4689 FLOAT,J4704 FLOAT,J4751 FLOAT,J4755 FLOAT,J6098 FLOAT,J6178 FLOAT,J9602 FLOAT,J9735 FLOAT,J9766 FLOAT,J1605 FLOAT,J3101 FLOAT,J3103 FLOAT,J3401 FLOAT,J3402 FLOAT,J3861 FLOAT,J3863 FLOAT,J3405 FLOAT,J3407 FLOAT,J4004 FLOAT,J4005 FLOAT,J4021 FLOAT,J4042 FLOAT,J4043 FLOAT,J4061 FLOAT,J4063 FLOAT,J4183 FLOAT,J4188 FLOAT,J4208 FLOAT,J4272 FLOAT,J4452 FLOAT,J4631 FLOAT,J4901 FLOAT,J4911 FLOAT,J6988 FLOAT,J5019 FLOAT,J5020 FLOAT,J5101 FLOAT,J5108 FLOAT,J5201 FLOAT,J5202 FLOAT,J5214 FLOAT,J5232 FLOAT,J5233 FLOAT,J5301 FLOAT,J5332 FLOAT,J5333 FLOAT,J5401 FLOAT,J5406 FLOAT,J5411 FLOAT,J5541 FLOAT,J3436 FLOAT,J5703 FLOAT,J5706 FLOAT,J5707 FLOAT,J5711 FLOAT,J5713 FLOAT,J5714 FLOAT,J5801 FLOAT,J5802 FLOAT,J5803 FLOAT,J5901 FLOAT,J2768 FLOAT,J8001 FLOAT,J8002 FLOAT,J8015 FLOAT,J8031 FLOAT,J8053 FLOAT,J8058 FLOAT,J1721 FLOAT,J1801 FLOAT,J1802 FLOAT,J1803 FLOAT,J1808 FLOAT,J1812 FLOAT,J1925 FLOAT,J1928 FLOAT,J1963 FLOAT,J5631 FLOAT,J6103 FLOAT,J6113 FLOAT,J6301 FLOAT,J6302 FLOAT,J6305 FLOAT,J6326 FLOAT,J6361 FLOAT,J6367 FLOAT,J6471 FLOAT,J6472 FLOAT,J6473 FLOAT,J7004 FLOAT,J7011 FLOAT,J7013 FLOAT,J7003 FLOAT,J7012 FLOAT,J7832 FLOAT,J7911 FLOAT,J7912 FLOAT,J7951 FLOAT,J3289 FLOAT,J8801 FLOAT,J8802 FLOAT,J8804 FLOAT,J8830 FLOAT,J9001 FLOAT,J9005 FLOAT,J9007 FLOAT,J9008 FLOAT,J9009 FLOAT,J9020 FLOAT,J9021 FLOAT,J9022 FLOAT,J9062 FLOAT,J9064 FLOAT,J9101 FLOAT,J9104 FLOAT,J9107 FLOAT,J9202 FLOAT,J9301 FLOAT,J9501 FLOAT,J9502 FLOAT,J9503 FLOAT,J9531 FLOAT,J9532 FLOAT, LastTime timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP ) engine=InnoDB  charset=utf8;
