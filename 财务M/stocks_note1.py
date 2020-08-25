
import requests
import re
import pymysql
from multiprocessing import Pool
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

def parse_all_pages_one(html):  # 不要一次把正则弄伤了
    try:

        patt = re.compile('<td class="txtcenter"><a href=".*?">(.*?)</a></td>' +'.*?<td class="txtcenter yjSt">(.*?)</td>'+
                          '.*?<td class="normal yjSt">(.*?)</td>'+'.*?<td class="txtright bold">(.*?)</td>'+
                          '.*?<td class="txtright bgyellow01">(.*?)</td>',re.S)
        items = re.findall(patt,html)
        big_list = []
        for item in items:
            big_list.append(item)
        return big_list
    except  TypeError as e:
        print(TypeError)



def insertDB(content):
    connection = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='123456', db='JS',
                                 charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)
    cur = connection.cursor()
    cur.executemany('insert into js_infos (coding,location,name,last_price,net_value) values (%s,%s,%s,%s,%s)', content)
    connection.commit()
    connection.close()
    print('向MySQL中添加数据成功！')



if __name__ == '__main__':

    for offset in range(1,75):
        url = 'https://info.finance.yahoo.co.jp/ranking/?kd=53&tm=d&vl=a&mk=1&p=' + str(offset)
        html = call_page(url)
        content =parse_all_pages_one(html)
        insertDB(content)
        print(offset)

# #
# create table js_infos(
# id int not null primary key auto_increment,
# coding varchar(11),
# location varchar(11),
# name text,
# last_price text,
# net_value text
# ) engine=InnoDB default charset=utf8;


# drop table js_infos;