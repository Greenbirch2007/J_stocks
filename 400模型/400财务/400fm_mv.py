import os

import pymysql
import csv

# 数据处理好，看如何塞入execl中


def csv_dict_write(path,head,data):
    with open(path,'w',encoding='utf-8',newline='') as f:
        writer = csv.DictWriter(f,head)
        writer.writeheader()
        writer.writerows(data)
        return True



if __name__ =='__main__':
    connection = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='123456', db='JS',
                                 charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)
    cur = connection.cursor()

    # sql 语句
    count_sql = "select count(*) from js_infos_finanData; "
    cur.execute(count_sql)
    # sql 语句
    big_list = []
    _400_s_pool = "6920,8424,3549,8593,8439,2331,6877,3003,8905,2127,7974,4684,4768,4091,3254,3769,9086,3141,7649,3148,5929,8111,7419,9065,9697,3288,8056,4528,7309,6750,7532,3626,3107,8279,4519,4568,8331"
    l_spool = _400_s_pool.split(",")
    for num in l_spool:
        sql = 'select title,coding,industry,market_value,returns_ratio from js_infos_finanData where coding in({0}) order by returns_ratio desc;'.format(num)
        #执行sql语句
        cur.execute(sql)
        # #获取所有记录列表
        data = cur.fetchone()
        big_list.append(data)
    print(big_list)
    l_path = os.getcwd()
    head = ['title','coding',"industry","market_value","returns_ratio"]
    csv_dict_write('{0}\\400js_SMV.csv'.format(l_path),head,big_list)
    print("数据导出完成～")

