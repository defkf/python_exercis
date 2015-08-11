#!/usr/bin/python  
#-*- coding=utf-8-*-   

'''获取音悦台，推荐乐单'''

import urllib2,sys
from bs4 import BeautifulSoup
#转码
reload(sys)
sys.setdefaultencoding('utf-8')

#乐单地址
url = 'http://v.yinyuetai.com/playlist/3861610'

html = urllib2.urlopen(url)
soup = BeautifulSoup(html)
p = soup.findAll('p',{'class':'mr_t80'} )
for i in p:
	txt = i.get_text()
	#写入music.txt文件
	op = open('music.txt' , 'a').write('\n' + txt)

print 'over'