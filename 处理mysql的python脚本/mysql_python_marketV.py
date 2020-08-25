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
    s_pool = '9629,4832,5922,6368,6920,2685,8747,3941,7518,2130,9873,4848,1946,6035,5440,9742,3254,7004,3186,3769,6754,3479,4996,8111,1909,1419,1885,6677,5410,9889,4483,2445,3107,9783,4519,8356,8524'
    l_spool = s_pool.split(",")
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
csv_dict_write('{0}\\js_SMV.csv'.format(l_path),head,big_list)
print("数据导出完成～")

