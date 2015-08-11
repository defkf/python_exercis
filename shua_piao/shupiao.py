#!/usr/bin/env python  
#-*- coding=utf-8-*-  

import urllib,urllib2

url = 'http://vote.pyfck.com/'
#设置代理ip
proxies = urllib2.ProxyHandler({'http':'http://116.246.6.52:80'})
httpHandler = urllib2.HTTPHandler(debuglevel=1)
opener = urllib2.build_opener(proxies)#编译代理ip
urllib2.install_opener(opener)#装载代理ip
#设置post参数
data = {'c':'main','a':'vote','id':'1'}
dataa = urllib.urlencode(data)#编译post参数
#设置头部信息
head = {'User-Agent':'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'}
#发送post
req = urllib2.Request(url , dataa , head)
#打开返回值
request = urllib2.urlopen(req).read().decode('gbk').encode('utf-8')
print request







