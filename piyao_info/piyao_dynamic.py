import json
import urllib
from urllib import request
import jsonpath
from bs4 import BeautifulSoup

class CrawingInfo():
    def __init__(self, pgnum, callback_num):
        self.pgnum = pgnum
        self.callback_num=callback_num
        self.headers={
            'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36',
            'Referer': 'http://www.xinhuanet.com/food/sppy/qwpy.htm',
            'Request URL': 'http://qc.wa.news.cn/nodeart/list?nid=11148362&pgnum={}&cnt=10&tp=1&orderby=1?callback=jQuery112401431122865743193_1563187623741&_{}'.format(self.pgnum,self.callback_num),
            # 'Content-Encoding':'UTF-8'
        }

    def craw_data(self, pgnum, callback_num):
        url = "http://qc.wa.news.cn/nodeart/list?nid=11148362&pgnum={}&cnt=10&tp=1&orderby=1?callback=jQuery112401431122865743193_1563187623741&_{}".format(self.pgnum,self.callback_num)

        try:
            with request.urlopen(url,timeout=10) as js:
                
                content = js.read()
                jsobj = json.loads(content)   #将json转化成python对象

                title = jsonpath.jsonpath(jsobj,'$..Title')
                linkurl = jsonpath.jsonpath(jsobj,'$..LinkUrl')
                pubtime = jsonpath.jsonpath(jsobj,'$..PubTime')
                editor = jsonpath.jsonpath(jsobj,'$..Editor')
                sourcename = jsonpath.jsonpath(jsobj,'$..SourceName')

                yaoyan_info = zip(title, linkurl, pubtime, editor, sourcename)
        except:
            content = None
            print('crawl data exception.')

        print(yaoyan_info) 
    
    # def get_content(self, yaoyan_info):

    #     url_list = yaoyan_info[1]

    #     for url in url_list:

    def go(self):

        pgnum = 1
        callback_num = 1563187623742

        while True:
            if(pgnum>4):
                return
            self.craw_data(pgnum,callback_num)
            pgnum+=1
            callback_num+=1

if __name__ == "__main__":
    CrawingInfo(1, 1563187623742)
    pass


