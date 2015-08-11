#!/usr/bin/env python  
#-*- coding=utf-8 -*-   


import spynner,pyquery,time,urllib2
from bs4 import BeautifulSoup

lis = []
url = 'http://www.u17.com/comic/195.html'

html = urllib2.urlopen(url).read()
soup = BeautifulSoup(html)
zi_len = soup.find('ul',id = 'chapter').find_all('a')
for s in zi_len:
	lis.append(s.get('href'))

# def len(url_lis):
# 	browser = spynner.Browser()
# 	browser.create_webview()
# 	browser.load(url_lis)

# 	string = browser.html
	
# 	soup = BeautifulSoup(string)
# 	return soup

# for i in lis:
# 	img = len(i).find_all('div',{'class':'pane'})
# 	for i in img:
# 		lenn = len(i.find_all('a'))
# 		print lenn

print lis





