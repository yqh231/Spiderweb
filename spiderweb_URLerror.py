import urllib2
request=urllib2.Request('http://www.xxx.com')

try:
    urllib2.urlopen(request,timeout=5)
except urllib2.URLError,s:
    print s.reason