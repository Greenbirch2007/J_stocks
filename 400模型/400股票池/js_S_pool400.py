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
    pool_data400 =(6920,8424,3549,8593,8439,2331,6877,3003,8905,2127,7974,4684,4768,4091,3254,3769,9086,3141,7649,3148,5929,8111,7419,9065,9697,3288,8056,4528,7309,6750,7532,3626,3107,8279,4519,4568,8331)
    for coding in pool_data400:
        call_url(coding)
        print(coding)
    print("图片下载完毕")
