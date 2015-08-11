#!/usr/bin/env python  
#-*- coding=utf-8-*-  

# url = 'https://www.baidu.com/'
#打开浏览器
# browser = spynner.Browser()
#打开浏览器窗口
# browser.show()
#读入URL
# browser.load(url)
#写东西进表单，（输入要搜索的值）
# browser.wk_fill('input[class="s_ipt"]','123')
#点击哪个按钮，（比如搜索）
# browser.wk_click('input[id="su"]',wait_load=True)
#等待多少时间
# browser.wait(6)
#关闭浏览器
# browser.close()

from bs4 import BeautifulSoup 
import urllib,urllib2,spynner

lis = []
url = 'http://www.u17.com/chapter/291.html#image_id=2341'
browser = spynner.Browser()
browser.create_webview()
browser.load(url)
x = 0
while x < 10:
	browser.wk_click('a[class="next"]')
	browser.wait(0.5)
	string = browser.html
	soup = BeautifulSoup(string)
	img = soup.find_all('img')
	for i in img:
		lis.append(i.get('src'))
	x += 1
l2 = sorted(set(lis),key=lis.index)
print l2
# browser.close()



