#!/usr/bin/env python  
#-*- coding=utf-8-*-
#"http://www.u17.com/chapter/291.html#image_id=2341"

from bs4 import BeautifulSoup 
import urllib,urllib2,os,spynner,pyquery,time


x = 0
'''browser = spynner.Browser()
#创建一个浏览器并把他赋值给browser
browser.create_webview()
#创建一个当前的QWebView对象并且插入当前的QWebPage
browser.set_html_parser(pyquery.PyQuery)
browser.load("http://www.u17.com/chapter/291.html#image_id=2341")
sstring = browser.html
while x < 10 :
    soup = BeautifulSoup(string)
    img = soup.find_all('img')
    for i in img:
        xlist.append(i.get('id'))
    nextp = xlist[2][8:]
    url = 'http://www.u17.com/chapter/291.html#image_id='+ nextp
    x += 1
    print url
while x < 10:
    nex = BeautifulSoup(url)
    img = soup.find_all('img')
    for a in img:
        print a.get('src')
    x += 1
print 'over'''

url = "http://www.u17.com/chapter/291.html#image_id=2343"

req = urllib2.Request(url)

res_data = urllib2.urlopen(req)
res = res_data.read()
print res














    
