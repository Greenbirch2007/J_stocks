import os

import pymysql
import csv
import csv
import datetime

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
# 数据处理好，看如何塞入execl中

# 读取code---形成fm----筛选股票池----定池子----跟踪模型与模板


def csv_dict_write(path,head,data):
    with open(path,'w',encoding='utf-8',newline='') as f:
        writer = csv.DictWriter(f,head)
        writer.writeheader()
        writer.writerows(data)
        return True
def read_xlrd(excelFile):
    data = xlrd.open_workbook(excelFile)
    table = data.sheet_by_index(0)
    dataFile = []
    for rowNum in range(table.nrows):
        dataFile.append(table.row_values(rowNum))

       # # if 去掉表头
       # if rowNum > 0:

    return dataFile



if __name__ =='__main__':
    lpath = os.getcwd()
    j225_allcode =[]
    excelFile = '{0}\\225_code.xlsx'.format(lpath)
    full_items = read_xlrd(excelFile=excelFile)
    for item in full_items:
        j225_allcode.append(str(item[0])[:-2])

    connection = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='123456', db='JS',
                                 charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)
    cur = connection.cursor()

    # sql 语句
    count_sql = "select count(*) from js_FinData; "
    cur.execute(count_sql)
    long_count = cur.fetchone()['count(*)']
    # sql 语句
    big_list = []
    for num in range(1, long_count):


        sql = 'select name,d2018,d2017,d2016,industry from js_FinData where id = %s ' % num
        # #执行sql语句
        cur.execute(sql)
        # #获取所有记录列表
        data = cur.fetchone()
        print(data["name"][-5:-1])
        if data["name"][-5:-1] in j225_allcode:
            big_list.append(data)
        else:
            pass

    print(big_list)
    l_path = os.getcwd()
    head = ['industry','name',"d2018","d2017","d2016"]
    csv_dict_write('{0}\\225js_data.csv'.format(l_path),head,big_list)
    print("数据导出完成～")
