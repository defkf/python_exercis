#!/usr/bin/env python  
#-*- coding=utf-8-*-   

import urllib

cont = raw_input('输入要搜索的内容：')
url_hou = urllib.quote(cont)
url_qian = 'http://my.68design.net/search/works?word='
url = url_qian + url_hou

print url


