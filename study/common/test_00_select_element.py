#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author:     dingyj
@contact:    june.diny@gmail.com
@others:     DTStudio, All rights reserved-- Created on 2016/11/17
@desc:      选择下拉框
这里的下拉框是通过html中<select>标签实现
"""
import os
from selenium import webdriver
from selenium.webdriver.support.ui import Select

path = os.getcwd()
path = 'file://' + path.split('test_case')[0] + 'demo_html' + os.sep + 'test.html'
demo_page = path.decode('gbk').encode('utf-8')


dr = webdriver.Firefox()
dr.implicitly_wait(30)
dr.get(demo_page)

sele = Select(dr.find_element_by_id("selectdemo"))
sele.select_by_visible_text("Volvo")
# sele.select_by_index()
# sele.select_by_value()
# 思考上面几个方法的区别

# 读取所有选项值
print("all options:")
opt = sele.options
for o in opt:
    print(o.text)

# 读取已选上的值
print("all selected options:")
apt = sele.all_selected_options
for a in apt:
    print(a.text)

# 遍历选择每一个子项
for o in opt:
    sele.select_by_visible_text(o.text)

dr.quit()

