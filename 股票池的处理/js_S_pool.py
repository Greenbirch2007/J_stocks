# 1.股票池的相关数据
# 2.股票池子的走势图整理！
# 3.用execl函数提取代码　　=MID(B2,LEN(B2)-4,4)
import re
import time
import urllib.request

from retrying import retry
from urllib.error import URLError


def retry_if_io_error(exception):
    return isinstance(exception,URLError)

#  重复请求
@retry(retry_on_exception=retry_if_io_error)
def call_url(coding):
    url = 'https://chart.yahoo.co.jp/?code=' + str(coding) + '.T&tm=1y&type=c&log=off&size=m&over=m65,m130,s&add=v&comp='
    urllib.request.urlretrieve(url, '/home/w/js_pic/%s.jpg' % coding)




if __name__=='__main__':

# 2020.1.28
    pool_data =(7172,5310,6480,9984,6706,6332,3482,6976,3990,3267,5271,9302,6951,2491,3053,9706,8111,8052,9104,8892,2471,7522,5288,3843,1871,6590,6569,7518,9880,3388,7718,2146,9629,9359,4427,6947,6544,6144,7509,3457,9658,6101,7731,5331,4921,6301,6235,5217,6155,5401,2114,2168,5357,6639,2003,9696,9797,9534,8885,7974,7609,3452,3300,3916,6200,9416,3186,3501,6161,7887,6513,6135,4776,8163,3150,6677,4553,6383,4996,3983,9519,5356,6998,2737,4238,4911,8699,3173,6055,6337,6324,9828,7537,8929,2317,4783,6121,4848,3254,2154,6815,3788,2427,4151,7717,2702,4023,9075,6143,7595,6850,9792,4552,5363)
    for coding in pool_data:
        call_url(coding)
        print(coding)
    print("图片下载完毕")
