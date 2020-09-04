# -*- coding: utf-8 -*-

# 读取页面文本
# 按照标题，保存整个文本


import csv
import datetime
import re
import time
import urllib.request

from retrying import retry
from urllib.error import URLError
import os
import os
import re
import time
import sys

type = sys.getfilesystemencoding()
import pymysql
import xlrd
import requests
from requests.exceptions import RequestException
from lxml import etree


def call_page(url):
    try:
        response = requests.get(url)
        response.encoding = 'utf-8'  #
        if response.status_code == 200:
            return response.text
        return None
    except RequestException:
        return None


def removeDot(item):
    f_l = []
    for it in item:
        f_str = "".join(it.split(","))
        f_l.append(f_str)

    return f_l


def remove_block(items):
    new_items = []
    for it in items:
        f = "".join(it.split())
        new_items.append(f)
    return new_items


def writerDt_csv(headers, rowsdata):
    # rowsdata列表中的数据元组,也可以是字典数据
    with open('tokyoTSN.csv', 'w', newline='') as f:
        f_csv = csv.writer(f)
        f_csv.writerow(headers)
        f_csv.writerows(rowsdata)


def read_xlrd(excelFile):
    data = xlrd.open_workbook(excelFile)
    table = data.sheet_by_index(0)
    dataFile = []
    for rowNum in range(table.nrows):
        dataFile.append(table.row_values(rowNum))

    # # if 去掉表头
    # if rowNum > 0:

    return dataFile












def retry_if_io_error(exception):
    return isinstance(exception,URLError)

#  重复请求
@retry(retry_on_exception=retry_if_io_error)
def call_url(coding):
    l_path = os.getcwd()
    url ='https://chart.yahoo.co.jp/?code={0}.T&tm=ay&type=c&log=off&size=m&over=m65,m130,s&add=v&comp='.format(coding)
    urllib.request.urlretrieve(url, '{0}/{1}.jpg'.format(l_path,coding))





#
if __name__=='__main__':
    lpath = os.getcwd()
    excelFile = '{0}\\js_bank.xlsx'.format(lpath)
    full_items = read_xlrd(excelFile=excelFile)
    for oneitem in full_items:
        f_code =str(oneitem[0])[:-2]


        call_url(f_code)
        print(f_code)
    print("图片下载完毕")



