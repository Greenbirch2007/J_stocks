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
    _225_s_pool = "7004,3863,4519,4568,4578,4523,7912,8804,2413,1721,9983,6361,8830,6976,4911,8802,2269,4021,7003,2801,1803,3382,6841,8331,1925,4452,8252,9433,4063,4503"
    l_spool = _225_s_pool.split(",")
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
    csv_dict_write('{0}\\225js_SMV.csv'.format(l_path),head,big_list)
    print("数据导出完成～")

