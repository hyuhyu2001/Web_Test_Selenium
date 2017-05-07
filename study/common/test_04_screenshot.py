#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author:     dingyj
@contact:    no19@foxmail.com, https://shop60459643.taobao.com
@others:     DTStudio, All rights reserved-- Created on 2016/11/10
@desc:        截图
"""
import os
import sys
from selenium import webdriver

path = os.getcwd()
path = 'file://' + path.split('test_case')[0] + 'demo_html' + os.sep + 'test.html'

demo_page = path.decode('gbk').encode('utf-8')


dr = webdriver.Firefox()
dr.maximize_window()
dr.implicitly_wait(30)
dr.get(demo_page)

dr.get_screenshot_as_file("D:\\screenshot.jpg")

dr.quit()