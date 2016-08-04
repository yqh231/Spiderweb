import urllib
import urllib2

values={"username":18706736571,"password":xxxxxx}
date=urllib.urlencode(values)
url="http://xxxxxxxxxxxx"
request=urllib2.Request(url,data)
response=urllib2.urlopen(request)
print response.read()