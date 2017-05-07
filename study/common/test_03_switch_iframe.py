#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author:     dingyj
@contact:    no19@foxmail.com, https://shop60459643.taobao.com
@others:     DTStudio, All rights reserved-- Created on 2016/11/10
@desc:       处理内嵌iframe
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

# dr.switch_to_frame("bdframe")   # 老版本selenium library
dr.switch_to.frame("bdframe")   # 新版本library

dr.find_element_by_id("kw").send_keys("selenium")
dr.find_element_by_id("su").click()
time.sleep(3)

# 在返回到原来的页面，即主页面
dr.switch_to.default_content()

# 勾选所有checkbox
books = dr.find_elements_by_name("book")
for book in books:
    book.click()

dr.find_element_by_id("submitOrder").click()

dr.quit()

# 如果没有下面这段代码，driver是找不到百度搜索框的
# dr.switch_to.frame("bdframe")


# 思考：如果一个页面包含多个iframe，改如何处理