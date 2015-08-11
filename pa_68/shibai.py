#!/usr/bin/env python  
#-*- coding=utf-8-*-   

from ghost import Ghost
from bs4 import BeautifulSoup 
import urllib,urllib2,os,spynner,re

os.chdir('G:\\img\\xz68')
os.getcwd


url = 'http://my.68design.net/search/works?word=%D2%F5%B5%C0%BD%F4%CB%F5'
#用beautifulsoup打开页面
def html(url):
	html = urllib2.urlopen(url).read()
	string = html.decode('gb2312').encode('utf-8') 	
	soup = BeautifulSoup(string)
	return soup
#返回所有列表url
def listt(urll):
	li = []
	u = 'http://my.68design.net'
	hre = html(urll).findAll('dl',{'class':'pall'})	
	for a in hre:
		for sr in a.find_all('a'):
			rr = re.compile(r'\/.+?\.html')
			m = re.match(rr,sr.get('href'))
			if m is not None:
				li.append(u + m.group())
	return li

def img_src(u):
	l = []
	sop = html(u).find('img',id='largeImg').get('src')
	return sop
#下载图片
def dowload(uurl):
	n = 0
	l1 =  listt(uurl)
	l2 = sorted(set(l1),key=l1.index)
	print '总共有 %s 张图片' %len(l2)
	for img in l2:
		sr = img_src(img)
		print '正在下载第 %s 张图片' %(n+1)
		req = urllib2.Request(str(sr))
		req.add_header('Referer',img)
		con = urllib2.urlopen(req).read()
		name = str(n) + '.jpg'
		n += 1
		f = open(name,'wb')
		f.write(con)
		f.close()


if __name__ == '__main__':
	dowload(url)

	print '下载完毕'