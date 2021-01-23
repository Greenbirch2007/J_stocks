


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
        f_jsp = ["J" + str(cod) for cod in jl]
        sp_func = lambda x: ",".join(x)
        f_lcode = sp_func(f_jsp)

        f_ls = "%s," * len(jl)+"%s,"# 这里错了
        fc = f_lcode+",J_index400"
        print(fc)
        print(f_ls[:-1])
        cursor.executemany('insert into sp_LJ_400 ({0}) values ({1})'.format(fc,f_ls[:-1]), content)
        connection.commit()
        connection.commit()
        connection.close()
        print('向MySQL中添加数据成功！')
    except TypeError:
        pass





# def get_index400():
#     url ='https://kabutan.jp/stock/?code=0040'
#     html =call_page(url)
#     element = etree.HTML(html)
#
#     now_price = element.xpath('//*[@id="stockinfo_i1"]/div[2]/span[2]/text()')
#     f_price = RemoveDot(remove_block(now_price))
#     return f_price



if __name__ == '__main__':
    #f_index400 = get_index400()

    jl = [1332,1333,1605,1719,1720,1721,1801,1802,1803,1808,1812,1820,1821,1824,1860,1861,1878,1881,1893,1911,1925,1928,1951,1959,2121,2124,2127,2146,2175,2181,2201,2206,2229,2267,2269,2282,2327,2331,2337,2371,2379,2412,2413,2427,2432,2433,2502,2503,2587,2651,2670,2702,2768,2782,2784,2801,2802,2809,2815,2871,2875,2897,2914,3003,3038,3048,3064,3086,3088,3092,3107,3116,3141,3148,3167,3197,3231,3254,3288,3289,3291,3349,3360,3382,3391,3401,3402,3405,3407,3436,3543,3549,3626,3659,3668,3738,3765,3769,3861,3932,4004,4005,4021,4042,4043,4061,4063,4088,4091,4151,4182,4183,4185,4188,4202,4204,4206,4208,4246,4307,4324,4403,4452,4502,4503,4506,4507,4516,4519,4521,4523,4528,4530,4536,4543,4555,4568,4578,4587,4612,4613,4631,4661,4666,4681,4684,4689,4704,4716,4732,4739,4751,4755,4768,4819,4849,4902,4911,4912,4922,4927,4967,5019,5020,5021,5101,5108,5110,5201,5233,5301,5332,5333,5334,5393,5401,5411,5486,5703,5713,5714,5801,5802,5929,5947,5975,6028,6098,6113,6136,6141,6146,6201,6268,6269,6273,6301,6302,6305,6324,6326,6367,6383,6432,6448,6463,6471,6473,6479,6481,6501,6503,6504,6506,6586,6588,6594,6641,6645,6701,6702,6723,6724,6728,6750,6752,6755,6758,6762,6770,6806,6841,6845,6849,6856,6857,6861,6869,6877,6902,6920,6923,6952,6954,6965,6971,6976,6981,6988,7011,7012,7013,7148,7164,7167,7186,7202,7203,7205,7259,7261,7267,7269,7270,7272,7276,7282,7309,7313,7419,7453,7458,7459,7532,7550,7564,7575,7606,7649,7701,7717,7729,7731,7733,7735,7741,7747,7751,7832,7846,7867,7951,7956,7974,7988,8001,8002,8015,8020,8028,8031,8035,8053,8056,8058,8088,8111,8113,8227,8252,8267,8273,8279,8282,8283,8303,8304,8306,8308,8309,8316,8331,8410,8411,8424,8439,8473,8570,8585,8591,8593,8601,8604,8628,8630,8697,8725,8750,8766,8795,8801,8802,8804,8830,8850,8876,8905,9001,9003,9005,9007,9008,9009,9020,9021,9022,9024,9041,9042,9045,9048,9062,9064,9065,9086,9201,9202,9404,9432,9433,9435,9437,9502,9503,9506,9508,9513,9531,9532,9602,9613,9627,9678,9684,9697,9706,9719,9735,9744,9766,9810,9843,9962,9983,9984,9989]

    big_list = []



    for it in jl:
        url = 'https://minkabu.jp/stock/{0}'.format(it)
        print(url)
        jsp = JSPool_M(url)# 这里把请求和解析都进行了处理
        jsp.page_parse_()
    ff_l = []
    f_tup = tuple(big_list)
    ff_l.append((f_tup))
    print(ff_l)
    insertDB(ff_l)
























 # create table sp_LJ_400(id int not null primary key auto_increment, J1332 FLOAT,J1333 FLOAT,J1605 FLOAT,J1719 FLOAT,J1720 FLOAT,J1721 FLOAT,J1801 FLOAT,J1802 FLOAT,J1803 FLOAT,J1808 FLOAT,J1812 FLOAT,J1820 FLOAT,J1821 FLOAT,J1824 FLOAT,J1860 FLOAT,J1861 FLOAT,J1878 FLOAT,J1881 FLOAT,J1893 FLOAT,J1911 FLOAT,J1925 FLOAT,J1928 FLOAT,J1951 FLOAT,J1959 FLOAT,J2121 FLOAT,J2124 FLOAT,J2127 FLOAT,J2146 FLOAT,J2175 FLOAT,J2181 FLOAT,J2201 FLOAT,J2206 FLOAT,J2229 FLOAT,J2267 FLOAT,J2269 FLOAT,J2282 FLOAT,J2327 FLOAT,J2331 FLOAT,J2337 FLOAT,J2371 FLOAT,J2379 FLOAT,J2412 FLOAT,J2413 FLOAT,J2427 FLOAT,J2432 FLOAT,J2433 FLOAT,J2502 FLOAT,J2503 FLOAT,J2587 FLOAT,J2651 FLOAT,J2670 FLOAT,J2702 FLOAT,J2768 FLOAT,J2782 FLOAT,J2784 FLOAT,J2801 FLOAT,J2802 FLOAT,J2809 FLOAT,J2815 FLOAT,J2871 FLOAT,J2875 FLOAT,J2897 FLOAT,J2914 FLOAT,J3003 FLOAT,J3038 FLOAT,J3048 FLOAT,J3064 FLOAT,J3086 FLOAT,J3088 FLOAT,J3092 FLOAT,J3107 FLOAT,J3116 FLOAT,J3141 FLOAT,J3148 FLOAT,J3167 FLOAT,J3197 FLOAT,J3231 FLOAT,J3254 FLOAT,J3288 FLOAT,J3289 FLOAT,J3291 FLOAT,J3349 FLOAT,J3360 FLOAT,J3382 FLOAT,J3391 FLOAT,J3401 FLOAT,J3402 FLOAT,J3405 FLOAT,J3407 FLOAT,J3436 FLOAT,J3543 FLOAT,J3549 FLOAT,J3626 FLOAT,J3659 FLOAT,J3668 FLOAT,J3738 FLOAT,J3765 FLOAT,J3769 FLOAT,J3861 FLOAT,J3932 FLOAT,J4004 FLOAT,J4005 FLOAT,J4021 FLOAT,J4042 FLOAT,J4043 FLOAT,J4061 FLOAT,J4063 FLOAT,J4088 FLOAT,J4091 FLOAT,J4151 FLOAT,J4182 FLOAT,J4183 FLOAT,J4185 FLOAT,J4188 FLOAT,J4202 FLOAT,J4204 FLOAT,J4206 FLOAT,J4208 FLOAT,J4246 FLOAT,J4307 FLOAT,J4324 FLOAT,J4403 FLOAT,J4452 FLOAT,J4502 FLOAT,J4503 FLOAT,J4506 FLOAT,J4507 FLOAT,J4516 FLOAT,J4519 FLOAT,J4521 FLOAT,J4523 FLOAT,J4528 FLOAT,J4530 FLOAT,J4536 FLOAT,J4543 FLOAT,J4555 FLOAT,J4568 FLOAT,J4578 FLOAT,J4587 FLOAT,J4612 FLOAT,J4613 FLOAT,J4631 FLOAT,J4661 FLOAT,J4666 FLOAT,J4681 FLOAT,J4684 FLOAT,J4689 FLOAT,J4704 FLOAT,J4716 FLOAT,J4732 FLOAT,J4739 FLOAT,J4751 FLOAT,J4755 FLOAT,J4768 FLOAT,J4819 FLOAT,J4849 FLOAT,J4902 FLOAT,J4911 FLOAT,J4912 FLOAT,J4922 FLOAT,J4927 FLOAT,J4967 FLOAT,J5019 FLOAT,J5020 FLOAT,J5021 FLOAT,J5101 FLOAT,J5108 FLOAT,J5110 FLOAT,J5201 FLOAT,J5233 FLOAT,J5301 FLOAT,J5332 FLOAT,J5333 FLOAT,J5334 FLOAT,J5393 FLOAT,J5401 FLOAT,J5411 FLOAT,J5486 FLOAT,J5703 FLOAT,J5713 FLOAT,J5714 FLOAT,J5801 FLOAT,J5802 FLOAT,J5929 FLOAT,J5947 FLOAT,J5975 FLOAT,J6028 FLOAT,J6098 FLOAT,J6113 FLOAT,J6136 FLOAT,J6141 FLOAT,J6146 FLOAT,J6201 FLOAT,J6268 FLOAT,J6269 FLOAT,J6273 FLOAT,J6301 FLOAT,J6302 FLOAT,J6305 FLOAT,J6324 FLOAT,J6326 FLOAT,J6367 FLOAT,J6383 FLOAT,J6432 FLOAT,J6448 FLOAT,J6463 FLOAT,J6471 FLOAT,J6473 FLOAT,J6479 FLOAT,J6481 FLOAT,J6501 FLOAT,J6503 FLOAT,J6504 FLOAT,J6506 FLOAT,J6586 FLOAT,J6588 FLOAT,J6594 FLOAT,J6641 FLOAT,J6645 FLOAT,J6701 FLOAT,J6702 FLOAT,J6723 FLOAT,J6724 FLOAT,J6728 FLOAT,J6750 FLOAT,J6752 FLOAT,J6755 FLOAT,J6758 FLOAT,J6762 FLOAT,J6770 FLOAT,J6806 FLOAT,J6841 FLOAT,J6845 FLOAT,J6849 FLOAT,J6856 FLOAT,J6857 FLOAT,J6861 FLOAT,J6869 FLOAT,J6877 FLOAT,J6902 FLOAT,J6920 FLOAT,J6923 FLOAT,J6952 FLOAT,J6954 FLOAT,J6965 FLOAT,J6971 FLOAT,J6976 FLOAT,J6981 FLOAT,J6988 FLOAT,J7011 FLOAT,J7012 FLOAT,J7013 FLOAT,J7148 FLOAT,J7164 FLOAT,J7167 FLOAT,J7186 FLOAT,J7202 FLOAT,J7203 FLOAT,J7205 FLOAT,J7259 FLOAT,J7261 FLOAT,J7267 FLOAT,J7269 FLOAT,J7270 FLOAT,J7272 FLOAT,J7276 FLOAT,J7282 FLOAT,J7309 FLOAT,J7313 FLOAT,J7419 FLOAT,J7453 FLOAT,J7458 FLOAT,J7459 FLOAT,J7532 FLOAT,J7550 FLOAT,J7564 FLOAT,J7575 FLOAT,J7606 FLOAT,J7649 FLOAT,J7701 FLOAT,J7717 FLOAT,J7729 FLOAT,J7731 FLOAT,J7733 FLOAT,J7735 FLOAT,J7741 FLOAT,J7747 FLOAT,J7751 FLOAT,J7832 FLOAT,J7846 FLOAT,J7867 FLOAT,J7951 FLOAT,J7956 FLOAT,J7974 FLOAT,J7988 FLOAT,J8001 FLOAT,J8002 FLOAT,J8015 FLOAT,J8020 FLOAT,J8028 FLOAT,J8031 FLOAT,J8035 FLOAT,J8053 FLOAT,J8056 FLOAT,J8058 FLOAT,J8088 FLOAT,J8111 FLOAT,J8113 FLOAT,J8227 FLOAT,J8252 FLOAT,J8267 FLOAT,J8273 FLOAT,J8279 FLOAT,J8282 FLOAT,J8283 FLOAT,J8303 FLOAT,J8304 FLOAT,J8306 FLOAT,J8308 FLOAT,J8309 FLOAT,J8316 FLOAT,J8331 FLOAT,J8410 FLOAT,J8411 FLOAT,J8424 FLOAT,J8439 FLOAT,J8473 FLOAT,J8570 FLOAT,J8585 FLOAT,J8591 FLOAT,J8593 FLOAT,J8601 FLOAT,J8604 FLOAT,J8628 FLOAT,J8630 FLOAT,J8697 FLOAT,J8725 FLOAT,J8750 FLOAT,J8766 FLOAT,J8795 FLOAT,J8801 FLOAT,J8802 FLOAT,J8804 FLOAT,J8830 FLOAT,J8850 FLOAT,J8876 FLOAT,J8905 FLOAT,J9001 FLOAT,J9003 FLOAT,J9005 FLOAT,J9007 FLOAT,J9008 FLOAT,J9009 FLOAT,J9020 FLOAT,J9021 FLOAT,J9022 FLOAT,J9024 FLOAT,J9041 FLOAT,J9042 FLOAT,J9045 FLOAT,J9048 FLOAT,J9062 FLOAT,J9064 FLOAT,J9065 FLOAT,J9086 FLOAT,J9201 FLOAT,J9202 FLOAT,J9404 FLOAT,J9432 FLOAT,J9433 FLOAT,J9435 FLOAT,J9437 FLOAT,J9502 FLOAT,J9503 FLOAT,J9506 FLOAT,J9508 FLOAT,J9513 FLOAT,J9531 FLOAT,J9532 FLOAT,J9602 FLOAT,J9613 FLOAT,J9627 FLOAT,J9678 FLOAT,J9684 FLOAT,J9697 FLOAT,J9706 FLOAT,J9719 FLOAT,J9735 FLOAT,J9744 FLOAT,J9766 FLOAT,J9810 FLOAT,J9843 FLOAT,J9962 FLOAT,J9983 FLOAT,J9984 FLOAT,J9989 FLOAT,LastTime timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP ) engine=InnoDB  charset=utf8;
