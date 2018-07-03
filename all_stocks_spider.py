
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

# url = 'https://info.finance.yahoo.co.jp/ranking/?kd=53&tm=d&vl=a&mk=1&p=1'
# html = call_page(url)



#解析页面  思考把代码做一个接口或队列，公用
# 所有个股链接，代码，名称，资本金
# def parse_all_pages(html):
#     patt = re.compile('<tr.*?href="(.*?)">(.*?)</a></td>' + '.*?<td class="normal yjSt">(.*?)</td>'+
#                       '.*?<td class="txtright bgyellow01">(.*?)</td>',re.S)
#     items = re.findall(patt,html)
#     for i in items:
#         data = pd.DataFrame([i[0],i[1],i[2],i[3]],index=['links','code','name','net assets'])
#         print(data)




# #
# parse_all_pages(html)

# url = 'https://stocks.finance.yahoo.co.jp/stocks/detail/?code=6178.t'
# html = call_page(url)
# selector=etree.HTML(html)

#解析一个个股页面
# code = selector.xpath('//*[@id="stockinf"]/div[1]/div[2]/dl/dt//text()')
# marker_value = selector.xpath('//*[@id="rfindex"]/div[2]/div[1]/dl/dd/strong//text()')
# share_nums = selector.xpath('//*[@id="rfindex"]/div[2]/div[2]/dl/dd/strong//text()')
# returns_ratio = selector.xpath('//*[@id="rfindex"]/div[2]/div[3]/dl/dd/strong//text()')
#
# data = pd.DataFrame({'code':code,"marker_value":marker_value,"share_nums":share_nums,'returns_ratio':returns_ratio})
# print(data)
#


url = 'https://kabutan.jp/stock/finance?code=3563&mode=k#zaimu_zisseki'
html = call_page(url)

# 个股的财务数据解析  又是表格数据！
