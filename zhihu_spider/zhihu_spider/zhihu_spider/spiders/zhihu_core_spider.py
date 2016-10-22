#! usr/bin/python
#coding=utf-8


import scrapy
import re
import os
import urllib
from scrapy.selector import Selector
import urllib2
from scrapy.spiders import CrawlSpider
import time
from scrapy.loader import ItemLoader
from zhihu_spider.items import ZhihuSpiderItem
from threading import Lock

sub_folder = os.path.join(os.getcwd(),"zhuhu_file")
if not os.path.exists(sub_folder):
	os.mkdir(sub_folder)
os.chdir(sub_folder)

class zhihu_spider(scrapy.Spider):

	name = "zhihu_spider"

	def __init__(self):

		self.path = 'D:\python\python_project\zhihu_spider\zhihu_spider\zhihu_spider\spiders\zhuhu_file'
		self.url_help = 'https://www.zhihu.com'
		self.answer_name = ' '
		self.count = 0
		self.mutex_lock = Lock()


	def start_requests(self):


		answer_nums = 0
		main_url = 'https://www.zhihu.com/node/ExploreAnswerListV2?params={"offset":'+str(answer_nums)+',"type":"day"}'
		
		while answer_nums < 50:

			print "get answer nums!!%s" % answer_nums
			yield scrapy.FormRequest(main_url,method='GET',formdata={"offset":str(50),"type":"day"},meta={'cookiejar': 1},callback=self.parse_first_page)
			time.sleep(1)
			answer_nums += 5
			


	def parse_first_page(self,response):

		selector = Selector(response)
		answer_urls = selector.xpath('body//link[@itemprop="url"]/@href').extract()

		for url in answer_urls:

			real_url = self.url_help + url
			print real_url
			yield scrapy.FormRequest(url=real_url ,callback=self.parse_answer_page)


	def parse_answer_page(self,response):

		loader = ZhihuSpiderItem()
		selector = Selector(response)

		self.answer_name = selector.xpath('head/title/text()').extract()[0]
		loader['answer_name'] = self.answer_name
		print self.answer_name

		answer_content_temp = selector.xpath('//div[@class="zm-editable-content clearfix"]/text()').extract("extract data failed!!")
		loader['answer_content'] = answer_content_temp

		image_content = response.xpath('''body//div[@class="zm-editable-content clearfix"]/img[@c
		lass="origin_image zh-lightbox-thumb lazy"]/@data-actualsrc''').extract()


		os.chdir(self.path)

		self.mutex_lock.acquire()

		try:
			folder_name = os.path.join(os.getcwd(),self.answer_name)
			time.sleep(1)
		except:
			folder_name = os.path.join(os.getcwd(),"error_name")

		if not os.path.exists(folder_name):

			try:
				os.mkdir(folder_name)
			except:
				os.mkdir("error_name")


		try:
			os.chdir(folder_name)
		except:
			pass

		self.mutex_lock.release()

		for image in image_content:
			self.count += 1
			self.save2file(image)


		yield item


	def save2file(self,image):

		fp = open(self.answer_name+'%s.jpg' %self.count ,'wb')
		data = urllib2.urlopen(image)
		fp.write(data.read())
		fp.close()
		print "now saving picture!!"
		#print image
		#urllib.urlretrieve(image,'zhihu_%s.jpg'%count)
		





		
