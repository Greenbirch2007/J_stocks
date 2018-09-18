




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
#特殊异常要先引入
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



#解析页面  思考把代码做一个接口或队列，公用
# 所有 coding, location,name,net_assets
def parse_all_pages_one(html):
    patt = re.compile('<td class="txtcenter"><a href=".*?">(.*?)</a></td>',re.S)
    items = re.findall(patt,html)
    for item in set(items):
        yield item


def parse_stock_note(url):
    try:

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
    except ValueError as e:
        raise e





def insertDB(content):
    connection = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='123456', db='j_stocks',
                                 charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)
    cursor = connection.cursor()
    try:
        cursor.executemany('insert into stocks_note2 (coding,industry,market_value,share_nums,returns_ratio,min_callMoney) values (%s,%s,%s,%s,%s,%s)', content)
        connection.commit()
        connection.close()
        print('向MySQL中添加数据成功！')
    except TypeError :
        pass

# 存在重复爬取的情况，还有就是会变动的数据还是要等到交易闭市之后再爬取，数据才不会变动！

# 3589条有遗漏，不知道是不是因为用了进程池的原因！
if __name__ == '__main__':
    pool = Pool(4)
    for offset in range(1,75):
        url = 'https://info.finance.yahoo.co.jp/ranking/?kd=53&tm=d&vl=a&mk=1&p=' + str(offset)
        html = call_page(url)
        Num = parse_all_pages_one(html)
        for item in set(Num):
            url = 'https://stocks.finance.yahoo.co.jp/stocks/detail/?code=%s.t' % item
            content = parse_stock_note(url)
            insertDB(content)
            print(url)





# create table stocks_note2(
# id int not null primary key auto_increment,
# coding varchar(11),
# industry varchar(11),
# market_value varchar(20),
# share_nums varchar(20),
# returns_ratio varchar(6),
# min_callMoney varchar(11)
# ) engine=InnoDB default charset=utf8;