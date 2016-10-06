#coding=gbk

#coding=utf-8

#-*- coding: UTF-8 -*-

import urllib2
import re
from lxml import etree
import os
import xlrd
import xlwt


class GetCsbook:

    def __init__(self,url):
        self.count=0
        self.book_name = []
        self.rating_nums = []
        self.author_names = []
        self.i=0
        self.j=0
        self.k=0

        while (self.count/20)<=95:
            final_url = url + "tag/编程?start=" +str(self.count) + "&type=T"
            self.count+=20
            self.GetHtml(final_url)
            print 'downloading %s page' , self.count/20




    def GetHtml(self,url):
        user_agent = "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0)"
        headers = {"User-Agent":user_agent}
        req = urllib2.Request(url,headers=headers)
        request = urllib2.urlopen(req)
        content = request.read()
        #print content
        self.parse_html(content)


    def parse_html(self,string):
        html = etree.HTML(string.lower().decode('utf-8'))
        book_names = html.xpath(u"/html/body//h2/a")
        rating_nums = html.xpath(u"/html/body//li//span[@class = 'rating_nums']")
        author_names1 = html.xpath(u"/html/body//div[@class = 'pub']")

        for book_name in book_names:
            self.book_name.append(book_name.text)

        for rating_num in rating_nums:
            self.rating_nums.append(rating_num.text)

        for author in author_names1:
            self.author_names.append(author.text)
        self.WriteToExcel()

    def WriteToExcel(self):

        for string_book_name in self.book_name[ self.i: ]:
            sheet.write(self.i,0,string_book_name)
            print string_book_name
            self.i+=1

        for string_rating_nums in self.rating_nums[ self.j: ]:
            sheet.write(self.j,1,string_rating_nums)
            self.j+=1

        for author in self.author_names[self.k : ]:
            sheet.write(self.k,2,author)
            self.k+=1





if __name__=='__main__':
    sub_folder = os.path.join(os.getcwd(), "MyWebProject")
    if not os.path.exists(sub_folder):
        os.mkdir(sub_folder)
    os.chdir(sub_folder)

    url = 'https://book.douban.com/'
    wbk = xlwt.Workbook()
    sheet = wbk.add_sheet('sheet 1')
    GetCsbook(url)
    wbk.save("D:\python\python_project\MyWebProject\computer books1.xls")

    print 'done'