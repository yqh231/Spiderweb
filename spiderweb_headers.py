import urllib
import urllib2

url='http://www.server.com/login'
user_agent='Mozilla/4.0 (compatible:MSIE 5.5; Windows NT)'
#如果网站有反盗链接,用以下headers
headers={'User-Agent':'Mozilla/4.0(compatible:MSIE 5.5:Windows NT)'
        ,'Refer':'http://www.zhihu.com/articles'}
values={'username':'cqc','password':'XXX'}
headers={'User-Agent':user_agent}
data=urllib.urlencode(values)
request=urllib2.Request(url,data,headers)
response=urllib2.urlopen(request)
page=response.read()
