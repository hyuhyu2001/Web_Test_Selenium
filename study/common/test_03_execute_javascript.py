#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author:     dingyj
@contact:    no19@foxmail.com, https://shop60459643.taobao.com
@others:     DTStudio, All rights reserved-- Created on 2016/11/10
@desc:        执行javascript
"""
import os
import sys
import time
from selenium import webdriver

path = os.getcwd()
path = 'file://' + path.split('test_case')[0] + 'demo_html' + os.sep + 'test.html'

demo_page = path.decode('gbk').encode('utf-8')

dr = webdriver.Firefox()
dr.implicitly_wait(30)
dr.maximize_window()
dr.get(demo_page)

# 将alertbutton的颜色变成蓝色
js = 'var d = document.getElementById("alertbutton"); d.style.background="#0a00fd"'
dr.execute_script(js)
time.sleep(3)

dr.quit()