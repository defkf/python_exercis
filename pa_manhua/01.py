#!/usr/bin/env python  
#-*- coding=utf-8-*-   

from bs4 import BeautifulSoup 
import urllib,urllib2,os,spynner,pyquery,time
os.chdir('F:\\img')
os.getcwd

browser = spynner.Browser()
#创建一个浏览器并把他赋值给browser
browser.create_webview()
#创建一个当前的QWebView对象并且插入当前的QWebPage
browser.load("http://www.u17.com/chapter/291.html#image_id=2341")
string = browser.html
soup = BeautifulSoup(string)
img = soup.find_all('img')
for i in img:
    print i.get('id')
#conn = urllib2.urlopen(img).read()
#f = open('name.jpg','wb')
#f.write(conn)
#f.close
#print " "
