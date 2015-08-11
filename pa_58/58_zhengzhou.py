#!/usr/bin/python
# -*- coding=utf-8 -*-

import urllib2,sys
from bs4 import BeautifulSoup 

reload(sys)
sys.setdefaultencoding('utf-8') 

def openn(u):
	html = urllib2.urlopen(u).read()
	soup = BeautifulSoup(html)
	return soup

def lis(ur):
	ll = []
	htm = openn(ur)
	clas = htm.find_all('a',{'class':'t'})
	for i in clas:
		ll.append(i.get('href'))
	return ll

def cont(urr):
	l = []
	for i in lis(urr):
		x = openn(i).find('span',{'class':'salaNum'}).get_text()
		l.append(x)
	return l

url = 'http://puyang.58.com/wangzhanmeigong/'

if __name__ == '__main__':
	# y = list(set(cont(url)))
	y = cont(url)
	a = float(y.count('2000-3000'))
	b = float(y.count('3000-5000'))
	c = float(y.count('面议'))
	d = float(len(y))

	print '共 : %s 个' %(d)
	print '2000-3000 : %s 个， 占%.2f%%' %(a,(a/d*100))
	print '3000-5000 : %s 个，  占%.2f%%' %(b,(b/d*100))
	print '面议 : %s 个， 占%.2f%%' %(c,(c/d*100))



