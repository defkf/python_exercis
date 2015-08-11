#!/usr/bin/env python  
#-*- coding=utf-8-*-   

from bs4 import BeautifulSoup 
import urllib,urllib2,os,re,sys



#根据用户输入内容合成url
cont = raw_input('Please enter the content:')
url_hou = urllib.quote(cont)
url_qian = 'http://my.68design.net/search/works?word='
url = url_qian + url_hou

#文件保存路径
wenjin = raw_input('Please enter a folder to save:')
os.chdir(wenjin)
os.getcwd


#用beautifulsoup打开页面
def html(url):
	html = urllib2.urlopen(url).read()
	string = html.decode('gb2312','ignore').encode('utf-8') 
	soup = BeautifulSoup(string)
	return soup

#返回所有列表的url
def listt(urll):
	li = []
	li2 = []
	li2.append(url)
	n = 2
	u = 'http://my.68design.net'
	ss = html(urll).find('div',{'class':'pagelist'}).find_all('a')
	#做判断总页数小于2的时候直接获取该页面列表url
	if len(ss) < 2:
		hre = html(urll).findAll('dl',{'class':'pall'})	
		for a in hre:
			for sr in a.find_all('a'):
				rr = re.compile(r'\/.+?\.html')
				m = re.match(rr,sr.get('href'))
				if m is not None:
					li.append(u + m.group())
	else:
		while n <= len(ss)-2:
			ht = urll + '&p=' + str(n)
			n += 1 
			li2.append(ht)
		for q in li2:
			hre = html(q).findAll('dl',{'class':'pall'})	
			for a in hre:
				for sr in a.find_all('a'):
					rr = re.compile(r'\/.+?\.html')
					m = re.match(rr,sr.get('href'))
					if m is not None:
						li.append(u + m.group())
	return li
#提取所有页面图片的src
def img_src(u):
	l = []
	sop = html(u).find('img',id='largeImg').get('src')
	return sop
# 下载图片
def dowload(uurl):
	n = 0
	l1 =  listt(uurl)
	l2 = sorted(set(l1),key=l1.index)

	print 'There are  %s pictures' %len(l2)
	for img in l2:
		sr = img_src(img)
		print 'Is being downloaded  %s copies' %(n+1)
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
	print 'OVER'
