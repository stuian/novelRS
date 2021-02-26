import requests
from lib.config import *
from bs4 import BeautifulSoup
from lxml import etree
import urllib
import json

def get_body(url,headers):
    """ 发送http请求 """
    retry_times = 0
    while retry_times < 3:
        try:
            content = requests.get(url, timeout=config['timeout'], headers=headers).text
            return content
        except KeyboardInterrupt:
            print("KeyboardInterrupt, now_url:", url)
            raise
        except:
            retry_times += 1
    return ''

def main():
    # baidu.com
    # word = "给芷若的青书"
    # file = word +".txt"
    # # site = "www.jjwxc.net"
    # url = 'http://www.baidu.com.cn/s?wd=' + urllib.parse.quote(word) + '&pn=0'+"&cl=3"#+"&si="+site
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.104 Safari/537.36"
    }
    # html = get_body(url,headers)
    # if html == "":
    #     raise Exception("Error download init url: %s" % url)
    # soup = BeautifulSoup(html, 'lxml')
    # tagh3 = soup.find_all('h3')
    # for h3 in tagh3:
    #     href = h3.find('a').get('href')
    #     print(href)
    #     with open(file, 'a', encoding='utf-8') as c:
    #         c.write(json.dumps(href, ensure_ascii=False) + '\n')

    #  quark
    link = "https://quark.sm.cn/s?q=%E9%BB%91%E8%8E%B2%E8%8A%B1%E6%94%BB%E7%95%A5%E6%89%8B%E5%86%8C"
    html = get_body(link, headers)
    print(html)





if __name__ == '__main__':
    main()