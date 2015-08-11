#!/usr/bin/env python  
#-*- coding=utf-8-*-   

from bs4 import BeautifulSoup
import urllib,urllib2,os

os.chdir("F:\\img")
os.getcwd
x = 0
urll = 'http://www.uisdc.com/'
def getHTML(url):
    page = urllib2.urlopen(url).read()
    return page
html = getHTML(urll)
soup = BeautifulSoup(html)
for i in soup.find_all('img'):
    link = i.get('src')
    print link
    name = str(x) + '.jpg'
    x += 1
    conn = urllib2.urlopen(link).read()

    '''f = open(name,'wb')
    f.write(conn)
    f.close
    print name'''
