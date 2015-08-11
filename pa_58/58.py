#!/usr/bin/python
# -*- coding=utf-8 -*-

import urllib2,sys
from bs4 import BeautifulSoup 

reload(sys)
sys.setdefaultencoding('utf-8') 
#打开网站
def openn(u):
	html = urllib2.urlopen(u).read()
	soup = BeautifulSoup(html)
	return soup
#获取页数以及地址
def page(uu):
	l = []
	url = openn(uu).find('div',{'class':'pager'}).find_all('a')
	for i in url:
		l.append('http://zz.58.com' + i.get('href'))
	return list(set(l))


#获取页面href
def lis(ur):
	ll = []
	for i in page(ur):
		htm = openn(i)
		clas = htm.find_all('a',{'class':'t'})
		for j in clas:
			ll.append(j.get('href'))
	return ll
#获取薪资数值
def cont(urr):
	l = []
	for i in lis(urr):
		x = openn(i).find('span',{'class':'salaNum'}).get_text()
		l.append(x)
	return l
#主页面url
url = 'http://ay.58.com/wangzhanmeigong/'

if __name__ == '__main__':
	y = cont(url)

	e = float(y.count('1000-2000'))
	a = float(y.count('2000-3000'))
	b = float(y.count('3000-5000'))
	f = float(y.count('5000-8000'))
	g = float(y.count('8000-12000'))
	c = float(y.count('面议'))
	d = float(len(y))


	print ' %s ' %(d)
	print '1000-2000 : %s ， %.2f%%' %(e,(e/d*100))
	print '2000-3000 : %s ， %.2f%%' %(a,(a/d*100))
	print '3000-5000 : %s ，  %.2f%%' %(b,(b/d*100))
	print '5000-8000 : %s ，  %.2f%%' %(f,(f/d*100))
	print '8000-12000 : %s ，  %.2f%%' %(g,(g/d*100))
	print 'interview : %s ， %.2f%%' %(c,(c/d*100))




