#!/usr/bin/env python  
#-*- coding=utf-8-*-   

from bs4 import BeautifulSoup 
import urllib,urllib2,os

url = 'http://www.u17.com'
html = urllib2.urlopen(url).read()
soup = BeautifulSoup(html)
contlist = []
zi_li = []
cont = soup.findAll('a',{'class':'comic_name'})
for i in cont:
        contlist.append(i.get('href'))
        title = i.get('title')
        print i.get('title'),' ', i.get('href')
for zilist in contlist:
        zi_html = urllib2.urlopen(zilist).read()
        zi_soup = BeautifulSoup(zi_html)
        zi_list = []
        zi_len = zi_soup.find('ul',id = 'chapter').find_all('a')
        for s in zi_len:
                zi_list.append(s.get('href'))
        zz = len(zi_list)
        zi_li.append(zz)
print zi_li

'''url = 'http://www.u17.com/comic/30067.html'
html = urllib2.urlopen(url).read()
soup = BeautifulSoup(html)
contlist = []
cont = soup.find('ul',id = 'chapter').find_all('a')
#print cont
for i in cont:
       contlist.append(i.get('href'))
print len(contlist)'''  

