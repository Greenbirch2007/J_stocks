# 1.股票池的相关数据
# 2.股票池子的走势图整理！
# 3.用execl函数提取代码　　=MID(B2,LEN(B2)-4,4)
import re
import time
import urllib.request

from retrying import retry
from urllib.error import URLError
import os


def retry_if_io_error(exception):
    return isinstance(exception,URLError)

#  重复请求
@retry(retry_on_exception=retry_if_io_error)
def call_url(coding):
    l_path = os.getcwd()
    url = 'https://chart.yahoo.co.jp/?code=' + str(coding) + '.T&tm=1y&type=c&log=off&size=m&over=m65,m130,s&add=v&comp='
    urllib.request.urlretrieve(url, '{0}/{1}.jpg'.format(l_path,coding))




if __name__=='__main__':

# 2020.1.28
    pool_data =(3258,6861,4182,5706,8035,3003,5713,4004,9983,1824,6632,5702,9766,9684,6268,6058,8909,7806,2127,8032,3092,2928,4506,4921)
    for coding in pool_data:
        call_url(coding)
        print(coding)
    print("图片下载完毕")
