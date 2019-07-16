import json
import urllib
from jsonpath import jsonpath
import requests

class CrawingInfo():

    def __init__(self, pgnum, callback_num, url):
        self.pgnum = pgnum
        self.callback_num=callback_num
        self.headers = {
            'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36',
        }
        self.url = "http://qc.wa.news.cn/nodeart/list?nid=11148362&pgnum={}&cnt=10&tp=1&orderby=1?callback=jQuery112401431122865743193_1563187623741&_{}".format(self.pgnum,self.callback_num)

    def craw_title(self):

        js = requests.get(self.url,headers=self.headers)
        content_bin = js.content
        content_str = content_bin.decode('utf8')
        content = content_str[42:-1]
        jsobj = json.loads(content)
        title = jsonpath(jsobj,'$..Title')
        js.close()

        return title
    
    def craw_linkurl(self):

        js = requests.get(self.url,headers=self.headers)
        content_bin = js.content
        content_str = content_bin.decode('utf8')
        content = content_str[42:-1]
        jsobj = json.loads(content)
        linkurl = jsonpath(jsobj,'$..LinkUrl')
        js.close()

        return linkurl

    def craw_pubtime(self):

        js = requests.get(self.url,headers=self.headers)
        content_bin = js.content
        content_str = content_bin.decode('utf8')
        content = content_str[42:-1]
        jsobj = json.loads(content)
        pubtime = jsonpath(jsobj,'$..PubTime')
        js.close()

        return pubtime

    def craw_editor(self):

        js = requests.get(self.url,headers=self.headers)
        content_bin = js.content
        content_str = content_bin.decode('utf8')
        content = content_str[42:-1]
        jsobj = json.loads(content)
        editor = jsonpath(jsobj,'$..Editor')
        js.close()

        return editor
            
    def craw_sourcename(self):

        js = requests.get(self.url,headers=self.headers)
        content_bin = js.content
        content_str = content_bin.decode('utf8')
        content = content_str[42:-1]
        jsobj = json.loads(content)
        sourcename = jsonpath(jsobj,'$..SourceName')
        js.close()

        return sourcename

    def go(self):

        while True:
            if(self.pgnum>4):
                return
            
            self.pgnum+=1
            self.callback_num+=1

if __name__ == "__main__":
    i = 1
    a = CrawingInfo(1, 1563187623742,"")
    while i<5:
        title=a.craw_title()
        sourcename = a.craw_sourcename()
        pubtime = a.craw_pubtime()
        url = a.craw_linkurl()
        editor = a.craw_editor()
        a.go()

        yaoyan_list = zip(title, sourcename, pubtime, url, editor)
        yaoyan_list = [j for j in yaoyan_list]

        for item in yaoyan_list:
            print('Title:', item[0])
            print('PubTime:', item[2])
            print('Source:', item[1])
            print('Editor',item[4])
            print('ContentURL:',item[3])
            print('\n')

    pass


