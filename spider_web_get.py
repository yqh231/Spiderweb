import urllib
import urllib2

values={}
values['username']='18706736571'
values['password']='xxx'
date=urllib.urlencode(values)
url="http://passportxxxxx"
geturl=url+"?"+data
request=urllib2.Request(geturl)
response=urllib2.urlopen(request)
print response.read()