#!/usr/bin/env python  
#-*- coding=utf-8-*-  


import Cookie,urllib,urllib2,cookielib
url = 'http://vote.pyfck.com/index.php?c=main&a=vote'

cookie_support= urllib2.HTTPCookieProcessor(cookielib.CookieJar())

proxies = urllib2.ProxyHandler({'http':'http://115.231.188.109:8080'})

opener = urllib2.build_opener(proxies,cookie_support, urllib2.HTTPHandler )
urllib2.install_opener(opener)


data = {'id':'1'}
dataa = urllib.urlencode(data)

head = {'User-Agent':'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'}

request = urllib2.Request(url , dataa , head)

html = urllib2.urlopen(request).read().decode('gbk').encode('utf-8')
print html



