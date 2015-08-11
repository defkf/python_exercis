#!/usr/bin/env python  
#-*- coding=utf-8-*-  

from bs4 import BeautifulSoup 
import urllib,urllib2,spynner,os

os.chdir('F:\\img')
os.getcwd
n = 0

ur = ['http://www.u17.com/chapter/291.html#image_id=2341'
,'http://www.u17.com/chapter/291.html#image_id=2342',
'http://www.u17.com/chapter/291.html#image_id=2343',
]

def img_src(url):
	lis = []
	browser = spynner.Browser()
	browser.create_webview()
	browser.load(url,20)

	string = browser.html
	soup = BeautifulSoup(string) 
	shuzi = soup.find_all('div',{'class':'pane'})
	for shu in shuzi:
		lenn = len(shu.find_all('a'))
	return lenn


	# x = 0
	# while x < lenn:
	# 	browser.wk_click('a[class="next"]')
	# 	browser.wait(0.1)
	# 	#string = browser.html
	# 	#soup = BeautifulSoup(string)
	# 	img = soup.find_all('img')
	# 	for i in img:
	# 		lis.append(i.get('src'))
	# 	x += 1
	# return lis
	# browser.close()
	
for w in ur:
	print img_src(w)

# l1 =  img_src(ur)
# l2 = sorted(set(l1),key=l1.index)
# print l2
# for i in l2:
# 	conn = urllib2.urlopen(i).read()
# 	name = str(n) + '.jpg'
# 	n += 1
# 	f = open(name,'wb')
# 	f.write(conn)
# 	f.close
# 	print 'over'


