

from lxml import etree
import requests
import re
from lxml import etree
import pandas as pd
import pymysql
from multiprocessing import Pool
# 解析尝试使用pyquery
from pyquery import PyQuery as pq
from lxml import etree




#请求页面

def call_page(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.text
        return None
    except RequestException:
        return None











url = 'https://kabutan.jp/stock/finance?code=3563&mode=k#zaimu_zisseki'

html = call_page(url)

doc = pq(url)
p = doc('#tbody > tr:nth-child(1) > th.fb_01')
# //*[@id="finance_box"]/table[3]/tbody/tr[3]/td[1]/span
# //*[@id="finance_box"]/table[3]/tbody/tr[4]/td[1]
#finance_box > table:nth-child(19) > tbody > tr:nth-child(3) > td:nth-child(1)
#finance_box > table:nth-child(19) > tbody > tr:nth-child(4) > td:nth-child(1)
#finance_box > table:nth-child(19) > tbody > tr:nth-child(1) > th.fb_01
print(doc)