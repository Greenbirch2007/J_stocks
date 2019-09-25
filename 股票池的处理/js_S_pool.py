# 1.股票池的相关数据
# 2.股票池子的走势图整理！
# 3.用execl函数提取代码　　=MID(B2,LEN(B2)-4,4)
import re
import time
import urllib.request






if __name__=='__main__':

    pool_data = (6969,7727,4506,3125,4422,5983,7897,4523,6736,4113,1739,6723,3528,1871,3854,9967,4588,7519,3668,3769,7647,1757,8894,4240,7567,7067,4584,3645,6898,3623)


    for coding in pool_data:
        url = 'https://chart.yahoo.co.jp/?code='+str(coding)+'.T&tm=1y&type=c&log=off&size=m&over=m65,m130,s&add=v&comp='
        urllib.request.urlretrieve(url, '/home/w/js_pic/%s.jpg' % coding)
        print(url)
    print("图片下载完毕")
