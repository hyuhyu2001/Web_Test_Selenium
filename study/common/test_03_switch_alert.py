#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author:     dingyj
@contact:    no19@foxmail.com, https://shop60459643.taobao.com
@others:     DTStudio, All rights reserved-- Created on 2016/11/10
@desc:        处理弹窗
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

dr.find_element_by_id("alertbutton").click()

# 打印弹出框提示语
alert = dr.switch_to.alert
print(alert.text)

# 点击弹出框上的确定按钮
alert.accept()
# alert.dismiss()

dr.quit()
