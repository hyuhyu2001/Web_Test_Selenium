#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author:     dingyj
@contact:    no19@foxmail.com, https://shop60459643.taobao.com
@others:     DTStudio, All rights reserved-- Created on 2016/11/10
@desc:
"""
import os
import sys
import time
from selenium import webdriver

path = os.path.abspath(os.path.dirname(sys.argv[0]))
path = 'file://' + path.split('test_case')[0] + 'demo_html' + os.sep + 'test.html'

demo_page = path.decode('gbk').encode('utf-8')


dr = webdriver.Firefox()
dr.maximize_window()
dr.implicitly_wait(30)
dr.get(demo_page)

# 勾选所有checkbox
books = dr.find_elements_by_name("book")
for book in books:
    book.click()

dr.find_element_by_id("submitOrder").click()

time.sleep(3)

dr.quit()
