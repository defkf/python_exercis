#!/usr/bin/env python  
#-*- coding=utf-8-*-   
from ghost import Ghost
from bs4 import BeautifulSoup 
import urllib,urllib2,os,spynner,re,time

url = 'http://my.68design.net/search/works?word=%C4%B8%C7%D7%BD%DA'
def html2(url):
	html = urllib2.urlopen(url).read()
	string = html
	soup = BeautifulSoup(string)
	return soup
def html(url):
	html = urllib2.urlopen(url).read()
	string = html.decode('gb2312').encode('utf-8') 
	soup = BeautifulSoup(string)
	return soup

def listt(urll):
	li = []
	li2 = []
	li2.append(url)
	n = 2
	u = 'http://my.68design.net'
	ss = html(urll).find('div',{'class':'pagelist'}).find_all('a')


	while n <= len(ss)-2:
		ht = urll + '&p=' + str(n)
		n += 1 
		li2.append(ht)

		
	print li2
	# for q in li2:
		
	# 	hre = html2(q).findAll('dl',{'class':'pall'})


	# 	for a in hre:
	# 		for sr in a.find_all('a'):
	# 			rr = re.compile(r'\/.+?\.html')
	# 			m = re.match(rr,sr.get('href'))
	# 			if m is not None:
	# 				li.append(u + m.group())
	# 				li.append(url)


	# return li
print listt(url)




# ss = html(url).find('div',{'class':'pagelist'}).find_all('a')

# n = 2
# if len(ss) < 2:
# 	pass
# else:
# 	while n <= len(ss)-2:
# 		ht = 'http://my.68design.net/search/works?word=%C4%B8%C7%D7%BD%DA&p=' + str(n)
# 		n += 1 
# 		print ht 



