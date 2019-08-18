# 1.股票池的相关数据
# 2.股票池子的走势图整理！
# 3.用execl函数提取代码　　=MID(B2,LEN(B2)-4,4)
import re
import time
import urllib.request

from lxml import etree
from selenium import webdriver


def get_one_page(url):

    driver.get(url)
    html = driver.page_source
    return html






if __name__=='__main__':

    pool_data = (9984,6301,5401,7974,4004,3436,7731,5301,6857,6383,6481,9104,6976,9706,6417,6135,6703,4553,3244,4819,7518,4921,9302,8111,8892,6754,2497,6235,6101,7718,2168,7172,1871,2146,6332,5331,1419,5310,6951,3315,3445,8052,4996,5288,1518,5357,9519,6480,6814,3388,2003,9534,6590,6125,3053,2491,7609,2737,9359,3452,5218,6144,3457,3501,6947,3843,2325,6569,3245,6706,6513,9416,7721,3482,6155,3182,6292,3250,6544,7725,6158,9880,9270,6639,6161,9658,3926,5217,3300,7887,4238,5356,3150,6467,2114,6142,7509,5271,7227,7726,9629,3990,9797,6191,8885,3655,9696,3983,4776,3916,7522,6998,8163,6855,8023)
    driver = webdriver.Chrome()

    for coding in pool_data:

        url = 'https://stocks.finance.yahoo.co.jp/stocks/chart/?code='+str(coding)+'.T&ct=z&t=1y&q=c&l=off&z=m&p=m65,m130,s&a=v'
        html = get_one_page(url)
        # 用正则会更精确一些！
        patt =re.compile('<div class="padT12 centerFi marB10"><img src="(.*?)" alt="チャート画像" /></div>',re.S)
        items  = re.findall(patt,html)
        for pi in items:
            urllib.request.urlretrieve(pi, '/home/w/js_pic/%s.jpg' % coding)
    driver.quit()
    print("图片下载完成！")


