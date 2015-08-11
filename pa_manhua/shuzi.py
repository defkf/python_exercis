#!/usr/bin/env python  
#-*- coding=utf-8-*-  

from bs4 import BeautifulSoup 
import urllib,urllib2,spynner,os



ur = ['http://www.u17.com/chapter/291.html#image_id=2341'
,'http://www.u17.com/chapter/291.html#image_id=2342',
'http://www.u17.com/chapter/291.html#image_id=2343',
]

for i in ur:
	string = urllib2.urlopen(i).read()
	soup = BeautifulSoup(string) 
	shuzi = soup.find_all('div',{'class':'pane'})
	print shuzi
	# for shu in shuzi:
	# 	lenn = len(shu.find_all('a'))
	# 	print lenn

