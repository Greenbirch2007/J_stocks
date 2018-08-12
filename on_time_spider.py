



import re
import datetime
import time
import requests
from pymongo import MongoClient




#使用一个字符串分割然后再拼接，去除掉分隔符号！


def get_index():
    response = requests.get('https://stocks.finance.yahoo.co.jp/stocks/detail/?code=998407.O')
    html = response.text
    patt = re.compile('<td class="stoksPrice">(.*?)</td>',re.S)
    item = re.findall(patt,html)
    for i in item:
        a = i.split(',')[0]
        b = i.split(',')[1]
        c = a + b
        big_list.append(c)



def get_stocks():
    response = requests.get('https://stocks.finance.yahoo.co.jp/stocks/detail/?code=8961.T')
    html = response.text
    patt = re.compile('<td class="stoksPrice">(.*?)</td>',re.S)
    item = re.findall(patt,html)
    for i in item:
        a = i.split(',')[0]
        b = i.split(',')[1]
        c = a + b
        big_list.append(c)

#浮点数

def get_spread():
    A = big_list[0]
    B = big_list[1]
    C = float(A)/float(B)
    W = "%.6f" % C
    big_list.append(W)



#尝试添加到三个不同的数据库看看哪个更好用！
# 先把爬取和存储的问题全部解决，后面再解决实时可视化的问题！
#highcharts，可视化就属于前端的部分了,慢慢来吧，监控工具改装一下，就是跟盘的工具！
#redis还是不适合多个键，多个值同时出现的场景！
def insert_to_Mongo(item):
    client = MongoClient(host='localhost',port=27017)   #链接连接数据库
    db = client.On_time_DT       #建立数据库
    p = db.ontime_dt            #在上面数据库中建立集合（表）
    result = p.insert(item)  # 添加内容
    print(result)



    # spread = int(A)/int(B)
    # big_list.append(spread)

if __name__ == '__main__':
    big_list = []
    while True:
        get_index()
        get_stocks()
        get_spread()
        con_dict = {
            'time':datetime.datetime.now(),
            'index':big_list[0],
            'stock':big_list[1],
            'spread':big_list[2],
        }
        insert_to_Mongo(con_dict)

        time.sleep(3)

        # l_tuple = tuple(big_list)
        # content = []
        # content.append(l_tuple)
        # print(content)



# python 字符与数字的转换：
# 整数字符串转换为对应的整数int('12')。
#
# 使用格式化字符串:
# tt=322
#
# tem='%d' %tt
#
# tem即为tt转换成的字符串
#
# 小数字符串转换为对应小数float('12.34')。
#
# double num1 = 0.0;String qq = "12.34";num1 = Double.valueOf(qq.toString());
#
# 数字转换为字符串str(123.45)。
#
# (123.45).to_bytes(4, 'big')
# b'\x13\x9b\xe5\x87'
# ASCII码转换为相应字符chr(97)。
#
# 字符转换为响应ASCII码ord('a')。