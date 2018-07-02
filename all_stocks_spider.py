
import requests
import re



#请求页面

def call_page(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            print(response.text)
        return None
    except RequestException:
        return None

url = 'https://info.finance.yahoo.co.jp/ranking/?kd=53&tm=d&vl=a&mk=1&p=1'
call_page(url)



#解析页面

def parse_one_page(html):
    patt = re.compile('')