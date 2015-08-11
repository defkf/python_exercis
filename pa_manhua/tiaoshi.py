#!/usr/bin/env python  
#-*- coding=utf-8-*-  

from bs4 import BeautifulSoup 
import urllib,urllib2,spynner,os,re

os.chdir("F:\\img\\1")
os.getcwd

n = 0

ur = ''

def img_src(url):
	lis = []
	m = 0
	browser = spynner.Browser()
	browser.show()
	browser.create_webview()
	browser.load(url,20)

	while m < 60:
		browser.wk_click('a[class="next"]')
		browser.wait(0.1)
		string = browser.html
		soup = BeautifulSoup(string)
		img = soup.find_all('img')
		for i in img:
			lis.append(i.get('src'))
		m += 1
		print '正在查找第 %s 页' %m
	return lis

x = 0
l1 =  img_src(ur)
l2 = sorted(set(l1),key=l1.index)
for i in l2:
	if i == 'none':
		pass
	else:
		conn = urllib2.urlopen(i).read()
		name = str(n) + '.jpg'
		n += 1
		f = open(name,'wb')
		f.write(conn)
		f.close
		x += 1
		print '正在下载第 %s 页' %x
