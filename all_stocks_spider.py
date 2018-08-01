
import requests
import re
from lxml import etree
import pandas as pd


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
CODING = []

#解析页面  思考把代码做一个接口或队列，公用
# 所有 coding, location,name,net_assets
# def parse_all_pages_one(html):
#     patt = re.compile('<td class="txtcenter"><a href=".*?">(.*?)</a></td>' +
#                       '.*?<td class="txtcenter yjSt">(.*?)</td>'+'.*?<td class="normal yjSt">(.*?)</td>'+
#                       '.*?<td class="txtright bgyellow01">(.*?)</td>',re.S)
#     items = re.findall(patt,html)
#     for item in items:
#         print(item)
#         CODING.append(item[0])
        # data = pd.DataFrame([i[0],i[1],i[2],i[3]],index=['links','code','name','net assets'])
        # print(data)
#
# url = 'https://info.finance.yahoo.co.jp/ranking/?kd=53&tm=d&vl=a&mk=1&p=1'
# html = call_page(url)
# parse_all_pages_one(html)

# #
# parse_all_pages(html)

url = 'https://stocks.finance.yahoo.co.jp/stocks/detail/?code=6178.t'
html = call_page(url)
selector=etree.HTML(html)


#解析一个个股页面



url = 'https://kabutan.jp/stock/finance?code=3563&mode=k#zaimu_zisseki'
html = call_page(url)

# 个股的财务数据解析  又是表格数据！
