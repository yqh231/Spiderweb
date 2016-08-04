import urllib2
request=urllib2.Request(url,data=data)
request.get_method=lambda:'PUT'#or 'DELETE'
response=urllib2.urlopen(request)