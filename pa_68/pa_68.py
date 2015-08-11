#!/usr/bin/env python  
#-*- coding=utf-8-*-   

from ghost import Ghost
from bs4 import BeautifulSoup 
import urllib,urllib2,os,spynner,re

#文件保存路径
os.chdir('G:\\img\\xz68\\gongjing')
os.getcwd


url = 'http://my.68design.net/search/works?word=%D7%D3%B9%AC%BC%A1%C1%F6'
#用beautifulsoup打开页面
def html(url):
	html = urllib2.urlopen(url).read()
	string = html.decode('gb2312').encode('utf-8') 	
	soup = BeautifulSoup(string)
	return soup
#返回所有列表的url
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
#用ghost模拟浏览器获取图片src
def ghost_img(src):
	ghost = Ghost()
	page,resources = ghost.open(src)
	ghost.wait_for_page_loaded()  
	result, resources = ghost.evaluate("document.getElementById('largeImg').getAttribute('src');" ) 
	del resources
	return result

# 下载图片
def dowload(uurl):
	n = 0
	l1 =  listt(uurl)
	l2 = sorted(set(l1),key=l1.index)
	print '总共有 %s 张图片' %len(l2)
	for img in l2:
		src = ghost_img(img)
		print '正在下载 第 %s 张图片' %(n+1)
		#模拟get请求，返回动态图片并下载至本地
		req = urllib2.Request(str(src))
		req.add_header('Referer',img)
		con = urllib2.urlopen(req).read()
		name = str(n) + '.jpg'
		n += 1
		f = open(name,'wb')
		f.write(con)
		f.close()
		
while 

if __name__ == '__main__':
	dowload(url)
	print '下载完毕'