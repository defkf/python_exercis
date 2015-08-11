#!/usr/bin/env python  
#-*- coding=utf-8-*-

from bs4 import BeautifulSoup 
import urllib,urllib2,os,spynner,pyquery,time

urll = 'http://www.u17.com/chapter/291.html#image_id=2341'
def html(url):
	browser = spynner.Browser()
	browser.create_webview()
	browser.load(url)
	string = browser.html
	#browser.close()
	soup = BeautifulSoup(string)
	return soup

def page_list(url1):
	listt = []
	img = html(urll).find_all('div',{'class':'pane'})
	for i in img:
		lenn = len(i.find_all('a'))
	x = int(url1[45:])
	i = 0
	while i < lenn:
		x += 1
		url2 = 'http://www.u17.com/chapter/291.html#image_id=' + str(x)
		i += 1
		listt.append(url2)
	return listt

# for c in page_list(urll):
# 	img_src = html(c).find_all('img')
# 	for a in img_src:
# 		print a.get('id')



if __name__ == '__main__':
	print page_list(urll)





