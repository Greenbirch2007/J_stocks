#-*- coding:utf-8 -*-
import re
import datetime
import time
import pymysql
import copy












def insertDB(content):
    connection = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='123456', db='JS',
                                 charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)
    cursor = connection.cursor()
    try:
        cursor.executemany("insert into Re_inDT (name,d2018,d2017,d2016,industry,coding,T_ind,market_value) values (%s,%s,%s,%s,%s,%s,%s,%s)", content)
        connection.commit()
        connection.close()
        print('向MySQL中添加数据成功！')
    except StopIteration :
        pass


if __name__ == "__main__":



    print(datetime.datetime.now())
    q1_list = []
    q2_list = []

    connection = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='123456', db='JS',
                                 charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)
    cursor = connection.cursor()



    # coding,location,name,last_price,net_value
    count_sql1 = "select count(*) from js_infos_finanData; "
    cursor.execute(count_sql1)
    long_count1 = cursor.fetchone()['count(*)']
    for page1 in range(1, long_count1 + 1):
        SQL_search1 = 'select coding,industry,title,market_value  from js_infos_finanData  where id = %s  ' % page1
        cursor.execute(SQL_search1)
        # #获取所有记录列表
        data1 = cursor.fetchone()
        q1_coding = data1["coding"]
        q1_location = data1["industry"]
        q1_name = data1["title"]
        q1_market_value = data1["market_value"]
        q1_list.append((q1_coding, q1_location, q1_name, q1_market_value))

    count_sql2 = "select count(*) from js_FinData; "
    cursor.execute(count_sql2)
    long_count2 = cursor.fetchone()['count(*)']
    for page2 in range(1, long_count2 + 1):
        SQL_search2 = 'select name,d2018,d2017,d2016,industry  from js_FinData  where id = %s  ' % page2
        cursor.execute(SQL_search2)
        # #获取所有记录列表
        data2 = cursor.fetchone()
        q2_name = data2["name"]
        q2_d2018 = data2["d2018"]
        q2_d2017 = data2["d2017"]
        q2_d2016 = data2["d2016"]
        q2_industry = data2["industry"]

        q2_list.append((q2_name, q2_d2018, q2_d2017, q2_d2016, q2_industry))


    # q1_coding,q1_location,q1_name,q1_market_value
    # q2_name,q2_d2018,q2_d2017,q2_d2016,q2_industry
    for item1 in q1_list:

        for item2 in q2_list:
            f_title = item2[0].split("【")[0]
            if item1[2] == f_title:
                f_tuple = item2+item1[:2]+item1[3:]
                print(f_tuple)
                insertDB([f_tuple])







# name,d2018,d2017,d2016,industry,coding,T_ind,market_value

# create table Re_inDT(
# id int not null primary key auto_increment,
# name varchar(50),
# d2018 varchar(20),
# d2017 varchar(20),
# d2016 varchar(20),
# industry varchar(8),
# coding varchar(11),
# T_ind varchar(60),
# market_value varchar(20)
# ) engine=InnoDB  charset=utf8;