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

# 2020.8.25
    pool_data =(4519,7004,1909,9873,5922,8747,5410,5440,1885,3941,6920,9629,7518,1419,3107,4996,6368,6754,4832,9889,3769,8356,8524,2130,9783,3254,4848,3186,1946,3479,2445,8111,6677,2685,9742,6035,4483)
    for coding in pool_data:
        call_url(coding)
        print(coding)
    print("图片下载完毕")
