




#
# 对一个列表迭代化之后，再有序的进行遍历
# for i in iter(list):
#     print(i)

from lxml import etree
import requests
import re
from lxml import etree
import pandas as pd
import pymysql
from multiprocessing import Pool

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

coding_list = []

#解析页面  思考把代码做一个接口或队列，公用
# 所有 coding, location,name,net_assets
def parse_all_pages_one(html):
    patt = re.compile('<td class="txtcenter"><a href=".*?">(.*?)</a></td>',re.S)
    items = re.findall(patt,html)
    for item in iter(items):
        coding_list.append(item)


def parse_stock_note(url):
    html = call_page(url)
    selector = etree.HTML(html)
    code = selector.xpath('//*[@id="stockinf"]/div[1]/div[2]/dl/dt//text()')
    industry = selector.xpath('//*[@id="stockinf"]/div[1]/div[2]/dl/dd[1]/a//text()')
    market_value = selector.xpath('//*[@id="rfindex"]/div[2]/div[1]/dl/dd/strong//text()')
    share_nums = selector.xpath('//*[@id="rfindex"]/div[2]/div[2]/dl/dd/strong//text()')
    returns_ratio = selector.xpath('//*[@id="rfindex"]/div[2]/div[3]/dl/dd/strong//text()')
    min_callMoney = selector.xpath('//*[@id="rfindex"]/div[2]/div[9]/dl/dd/strong//text()')
    stocks_note1 = tuple(code + industry + market_value + share_nums + returns_ratio + min_callMoney)
    stocks_Note2 = []
    stocks_Note2.append(stocks_note1)
    return stocks_Note2





def insertDB(content):
    connection = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='123456', db='j_stocks',
                                 charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)
    cursor = connection.cursor()
    cursor.executemany('insert into stocks_note2 (coding,industry,market_value,share_nums,returns_ratio,min_callMoney) values (%s,%s,%s,%s,%s,%s)', content)
    connection.commit()
    connection.close()
    print('向MySQL中添加数据成功！')




if __name__ == '__main__':
    pool = Pool(2)
    for offset in range(1,75):
        url = 'https://info.finance.yahoo.co.jp/ranking/?kd=53&tm=d&vl=a&mk=1&p=' + str(offset)
        html = call_page(url)
        parse_all_pages_one(html)
        for Num in iter(coding_list):
            url = 'https://stocks.finance.yahoo.co.jp/stocks/detail/?code=%s.t' % Num
            content = parse_stock_note(url)
            insertDB(content)
            print(offset)






# create table stocks_note2(
# id int not null primary key auto_increment,
# coding varchar(11),
# ind varchar(11),
# name text,
# net_assets text
# ) engine=InnoDB default charset=utf8;
#
