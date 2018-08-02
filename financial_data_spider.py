


#可以通过引入外部模块
# from list_package import list_pac
# for i in list_pac:
#     print(len(i))
#用bs4解析表格数据
import requests
import re
import pandas as pd
import pymysql
from multiprocessing import Pool
from bs4 import BeautifulSoup
from requests.exceptions import RequestException
import p


#请求页面

def call_page(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.text
        return None
    except RequestException:
        return None
#
# 标签嵌套结构 嵌套的结构更复杂  尝试用其他方法bs4也不要解析
# table --> tbody --->tr ---> th
# table --> tbody --->tr ---> td
#
# def parse_financial_page(html):
#     soup = BeautifulSoup(html,'lxml')
#     tables = soup.find_all('table')
#     # tbodys = []
#     # trs = []
#     tds = []
#     for table in tables:
#         for tbody in table:
#             # tbodys.append(tbody)
#             for tr in tbody:
#                 # trs.append(tr)
#                 for td in tr:
#                     tds.append(td.string)
#     print(tds)
#

#好久没用正则了，为啥不能批量匹配而值匹配了第一条
# 重复性的标签，如表格数据，按顺序写正则去匹配是无效的
def parse_one_page(html):
    patt = re.compile('<div class="cap1">３ヵ月業績の推移【実績】</div>'+'.*?<td>(.*?)</td>',re.S)

    item = re.findall(patt,html)
    for i in item:
        print(i)

# 重复性的标签，如表格数据，按顺序写正则去匹配是无效的,页面中同时有多个表格，糟心啊
# 爬取不利，就要重新思考数据源



url = 'https://kabutan.jp/stock/finance?code=3563&mode=k#zaimu_zisseki'

html = call_page(url)
parse_one_page(html)