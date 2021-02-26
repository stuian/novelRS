import requests
from bs4 import BeautifulSoup

def get_body(url):
    """ 发送http请求 """
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.104 Safari/537.36",
        'Cookie': 'timeOffset_o=-783.699951171875; smidV2=20210219113507c8b54bbb4ea430631e9668df2fdc3ac1000722678b27fe550; __yjs_duid=1_feaf616df4f88725480509f8f71af7321613902970817; UM_distinctid=177c41cff4119e-0d27c12b498d92-73e356b-100200-177c41cff42409; testcookie=yes; Hm_lvt_bc3b748c21fe5cf393d26c12b2c38d99=1613810729,1613810744,1613810872,1613826955; nicknameAndsign=2%7E%29%24%E8%92%8B%E8%92%8B; token=MjA0NzQ0OTd8ZmJjNGI1OTU1NTdlZGJlNmFmOWFiNzMwMmFiYTQyYzZ8fHx8NDMyMDB8MXx8fFFR55So5oi3fDB8dGVuY2VudHwx; JJEVER={"ispayuser":"20474497-0","foreverreader":"20474497","desid":"9gWNLcS2QWxjGpGUHEI8jlC31ys\/TH66","sms_total":"1","user_signin_days":"20210224_20474497_0"}; CNZZDATA30075907=cnzz_eid=519324035-1613703515-null&ntime=1614167919; JJSESS={"sidkey":"WwlICX3YxQJKhr0TjvGBNOq7c8PaZgbkH6","nicknameAndsign":"2%7E%29%24%E8%92%8B%E8%92%8B","clicktype":""}; Hm_lpvt_bc3b748c21fe5cf393d26c12b2c38d99=1614173255'
    }
    retry_times = 0
    while retry_times < 3:
        try:
            content = requests.get(url, timeout=10, headers=headers).text
            return content
        except KeyboardInterrupt:
            print("KeyboardInterrupt, now_url:", url)
            raise
        except:
            retry_times += 1
    return ''

class Novel:
    def __init__(self):
        self.novel_name = None
        self.novel_author = None
        self.abstract = None
        self.category = None
        self.view = None
        self.label = None
        self.style = None
        self.author_url = None
        self.novel_url = None

class GetNovel:
    def run(self):
        popular_url = "http://www.jjwxc.net/bookbase.php?fw0=0&fbsj0=0&ycx0=0&xx1=1&mainview0=0&sd0=0&lx0=0&fg0=0&bq=-1&removebq=&sortType=4&isfinish=2&collectiontypes=ors"
        # page_num = get_page_num(html)
        page_num = 100
        for page in range(1,page_num+1):
            url = popular_url + "&page=%d" % page
            novel_list_html = get_body(url)
            if novel_list_html == "":
                raise Exception("Error download init url: %s" % url)
            print(url)
            novels = self.parse(novel_list_html)

    def parse(self,html):
        soup = BeautifulSoup(html, "html.parser")
        # print(soup.find("table",{"class": "cytable"}))
        # print(soup.find("table",{"class": "cytable"}).find("tbody"))
        novel_list = soup.find("table",{"class": "cytable"}).find("tbody").find_all("tr")
        # print(novel_list)
        count = 0
        for novel_info in novel_list:
            if count != 0:
                book = Novel()
                novel_info_list = novel_info.find_all("td")
                # print(novel_info_list)
                for i, info in enumerate(novel_info_list):
                    if i == 0:
                        book.novel_author = info.find("a").get_text()
                        book.author_url = info.find("a").attrs["href"]
                    if i == 1:
                        book.novel_name = info.find("a").get_text()
                        book.novel_url = info.find("a").attrs["href"]
                        book.novel_url = "http://www.jjwxc.net/" + book.novel_url
                    if i == 2:
                        book.category = info.get_text().strip()
                    if i == 3:
                        book.style = info.get_text().strip()
                novel_html = get_body(book.novel_url)
                if novel_html == "":
                    raise Exception("Error download init url: %s" % book.novel_url)
                # book.abstract, book.view, book.label =
                self.parse_novel(novel_html)
            count += 1

    def parse_novel(self,html):
        soup = BeautifulSoup(html, "html.parser")
        print(soup.find("table"))

def main():
    books = GetNovel()
    books.run()

if __name__ == '__main__':
    main()

